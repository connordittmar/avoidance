class Obstacle(object):
    def __init__(self,lla,radius):
        self.lla = lla
        self.radius = radius

class AirStates(object):
    def __init__(self,plane_telemetry,object):
        self.plane_telemetry = plane_telemetry
        self.object = object

    def refresh(self):
        self.plane_telemetry = plane_telemetry
        self.object = object


class Dimensions(object):
    def __init__(self,safety_dist,scan_dist):
        self.safety_dist = safety_dist
        self.scan_dist = scan_dist
