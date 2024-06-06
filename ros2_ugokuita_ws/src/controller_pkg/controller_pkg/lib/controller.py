import struct
import threading
import time

digital_button = {'A':0, 'B':1, 'X':2, 'Y':3, 'LB':4, 'RB':5, 'Back': 6, 'Start': 7}
analog_button =  {'L_Axis_x':0, 'L_Axis_y':1, 'LT':2, 'R_Axis_x':3, 'R_Axis_y':4, 'RT':5, 'Cross_x':6, 'Cross_y':7}
class Joycon:

	def __init__(self, path):
		self.gamepad = open(path, "rb")

		self.state = {}

		self.t = threading.Thread(target = self.loop)
		self.t.start()

	def loop(self):
		while True:
			input = self.gamepad.read(8)
			_, value, digital_analog, index = struct.unpack("<Ihbb", input)
			if(digital_analog == 2):
				if(index == analog_button['L_Axis_x']):
					self.state['L_Axis_x'] = value
				elif(index == analog_button['L_Axis_y']):
					self.state['L_Axis_y'] = value
				elif(index == analog_button['LT']):
					self.state['LT'] = value
				elif(index == analog_button['R_Axis_x']):
					self.state['R_Axis_x'] = value
				elif(index == analog_button['R_Axis_y']):
					self.state['R_Axis_y'] = value
			elif(digital_analog == 1):
				if(index == digital_button['A']):
					self.state['A'] = value
				elif(index == digital_button['B']):
					self.state['B'] = value
				elif(index == digital_button['X']):
					self.state['X'] = value
				elif(index == digital_button['Y']):
					self.state['Y'] = value
				elif(index == digital_button['LB']):
					self.state['LB'] = value
				elif(index == digital_button['RB']):
					self.state['RB'] = value
				elif(index == digital_button['Back']):
					self.state['Back'] = value
				elif(index == digital_button['Start']):
					self.state['Start'] = value

	def get(self) -> dict:
		# left = self.clamp(self.l_axis_x - self.l_axis_y)
		# right = self.clamp(-self.l_axis_x - self.l_axis_y)
		return self.state

	# def clamp(self, n):
	# 	minimum_value = -32768
	# 	maximum_value = 32767
	# 	upper_clamped_value = min(n, maximum_value)
	# 	upper_lower_clamped_value = max(upper_clamped_value, minimum_value)
	# 	return upper_lower_clamped_value


def main():
	joycon = Joycon("/dev/input/js0")
	while True:
		print(joycon.get())
		time.sleep(0.5)

if __name__ == '__main__':
	main()
