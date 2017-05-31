from bin import gpsutils
from math import sqrt

def collision_check(plane_lla,object):
    helper = gpsutils.GpsUtils()
    safety_dist = 200
    enu = helper.lla2enu(object.lla,plane_lla)
    if(calc_dist(enu) < safety_dist + object.radius):
        return True
    else:
        return False

def calc_dist(enu):
    #arguments [east,north,up]
    east = enu[0]
    north = enu[1]
    up = enu[2]
    calc_dist = sqrt(east**(2) + north**(2) + up**(2))
    return calc_dist
