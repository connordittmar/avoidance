
from math import sqrt

def collision_check(plane_gps,objects):
    enu = []
    for object in objects:
        enu = gps2enu(plane_gps,object.location)
        if(calc_dist(enu) < safety_dist + object.radius):
            return True
    return False

def calc_dist(enu):
    #arguments [east,north,up]
    east = enu[0]
    north = enu[1]
    up = enu[2]
    calc_dist = sqrt(east**(2) + north**(2) + up**(2))
    return calc_dist
