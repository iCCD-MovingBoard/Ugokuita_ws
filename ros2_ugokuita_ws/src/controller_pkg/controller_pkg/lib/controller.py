import struct
import threading
import time

digital_button = {'A':0, 'B':1, 'X':2, 'Y':3, 'LB':4, 'RB':5, 'Back': 6, 'Start': 7}
analog_button =  {'L_Axis_x':0, 'L_Axis_y':1, 'LT':2, 'R_Axis_x':3, 'R_Axis_y':4, 'RT':5, 'Cross_x':6, 'Cross_y':7}
class Joycon:

	def __init__(self, path):
		self.gamepad = open(path, "rb")

		# analog
		self.l_axis_x = 0
		self.l_axis_y = 0
		self.lt = 0
		self.r_axis_x = 0
		self.r_axis_y = 0
		self.rt = 0
		self.cross_x = 0
		self.cross_y = 0

		# digital
		self.a_button = 0
		self.b_button = 0
		self.x_button = 0
		self.y_button = 0
		self.lb_button = 0
		self.rb_button = 0
		self.back_button = 0
		self.start_button = 0

		self.t = threading.Thread(target = self.loop)
		self.t.start()

	def loop(self):
		while True:
			input = self.gamepad.read(8)
			_, value, digital_analog, index = struct.unpack("<Ihbb", input)
			if(digital_analog == 2):
				if(index == analog_button['L_Axis_x']):
					self.l_axis_x = value
				elif(index == analog_button['L_Axis_y']):
					self.l_axis_y = value
				elif(index == analog_button['LT']):
					self.lt = value
				elif(index == analog_button['R_Axis_x']):
					self.r_axis_x = value
				elif(index == analog_button['R_Axis_y']):
					self.r_axis_y = value
				elif(index == analog_button['RT']):
					self.rt = value
				elif(index == analog_button['Cross_x']):
					self.cross_x = value
				elif(index == analog_button['Cross_y']):
					self.cross_y = value
			else:
				if(index == digital_button['A']):
					self.a_button = value
				elif(index == digital_button['B']):
					self.b_button = value
				elif(index == digital_button['X']):
					self.x_button = value
				elif(index == digital_button['Y']):
					self.y_button = value
				elif(index == digital_button['LB']):
					self.lb_button = value
				elif(index == digital_button['RB']):
					self.rb_button = value
				elif(index == digital_button['Back']):
					self.back_button = value
				elif(index == digital_button['Start']):
					self.start_button = value

	def get(self):
		left = self.clamp(self.l_axis_x - self.l_axis_y)
		right = self.clamp(-self.l_axis_x - self.l_axis_y)
		state = ''
		for key in digital_button:
			state += key + ':' + str(getattr(self, key.lower() + '_button')) + ','
		for key in analog_button:
			state += key + ':' + str(getattr(self, key.lower())) + ','
		return state[:-1]

	def clamp(self, n):
		minimum_value = -32768
		maximum_value = 32767
		upper_clamped_value = min(n, maximum_value)
		upper_lower_clamped_value = max(upper_clamped_value, minimum_value)
		return upper_lower_clamped_value


def main():
	joycon = Joycon("/dev/input/js0")
	while True:
		print(joycon.get())
		time.sleep(0.5)

if __name__ == '__main__':
	main()
