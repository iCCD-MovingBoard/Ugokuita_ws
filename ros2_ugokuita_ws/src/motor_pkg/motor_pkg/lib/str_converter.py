def to_str(byte_str):
    str = byte_str.decode('utf-8')
    return str

before_x_button = 0
def to_speeds(str):
    speeds_str = str.split(',')
    speeds = []
    for speed in speeds_str:
        # speed_str = speed.strip()
        speed: int = int(speed)
        speeds.append(speed)
    global before_x_button
    speed_dict = {'left': speeds[0], 'right': speeds[1], 'x_button': speeds[2] if len(speeds) == 3 else before_x_button}
    if len(speeds) == 3:
        before_x_button = speeds[2]
    return speed_dict