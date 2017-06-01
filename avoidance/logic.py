from bin import gpsutils
from math import sqrt, sin, cos, atan2

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
    
def diff_dist(obj1,obj2):
    if len(obj1==2):
        calc_dist = sqrt( abs(obj1[0]-obj2[0])**2 + abs(obj1[1]-obj2[1])**2 )
    elif len(obj1==3):
        calc_dist = sqrt( abs(obj1[0]-obj2[0])**2 + abs(obj1[1]-obj2[1])**2 + abs(obj1[2]-obj2[2])**2)
    else:
        raise "Input Must be two or three element float lists."


def find_wp_enu(enu,apparent_radius,heading,look_ahead_dist):
    #finds next waypoint after risk of collision becomes apparent
    x=look_ahead_dist*sin(heading) #heading must be in radians
    y=look_ahead_dist*cos(heading)
    enu_look_ahead= [x , y]

    for i in range(1,6): #i goes from 1 to 5
        heading_temp=heading-(.88*i)
        x=look_ahead_dist*sin(heading_temp) #heading must be in radians
        y=look_ahead_dist*cos(heading_temp) #heading must be in radians
        enu_look_ahead= [x , y]
        dr_dist=diff_distance(enu_look_ahead,enu) #finding the distance the projected point will be from the object
        if dr_dist > apparent_radius: #if distance to object is greater than safty dist and object radius
            break
        else:
            heading_temp=heading+(.88*i) #checking other direction
            x=look_ahead_dist*sin(heading_temp)
            y=look_ahead_dist*cos(heading_temp)
            enu_look_ahead= [x , y]
            dr_dist=diff_distance(enu_look_ahead,enu)
        if dr_dist > apparent_radius:
            break
    wp=enu_look_ahead
    return wp
