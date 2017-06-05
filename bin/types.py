class Obstacle(object):
    def __init__(self,lla,radius,enu=[0,0,0],speed=[0,0,0]):
        self.lla = lla
        self.radius = radius
        self.enu = enu
        self.speed = speed

class MovingObstacle(Obstacle):
    def update(self,dt):
        self.enu = [self.enu[0]+self.speed[0]*dt,self.enu[1]+self.speed[1]*dt,0]

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
