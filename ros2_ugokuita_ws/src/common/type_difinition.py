
CONTROLLER_ID = 0
REALSENCE_ID = 1
LIDAR_ID = 2

class RequestCommand():
    def __init__(self, id, r, l, h, b):
        self.id = id
        self.r = r
        self.l = l
        self.h = h
        self.b = b

class SendCommand():
    def __init__(self, r, l, h, b):
        self.r = r
        self.l = l
        self.h = h
        self.b = b

class RecieveCommand():
    def __init__(self, r, l):
        self.r = r
        self.l = l
