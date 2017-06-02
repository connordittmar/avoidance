from bin import gpsutils
from math import sqrt, sin, cos, atan2

def collision_check(enu_to_object,object_radius,safety_dist):
    if(calc_dist(enu_to_object) < safety_dist + object_radius):
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
    if len(obj1)==2:
        calc_dist = sqrt( abs(obj1[0]-obj2[0])**2 + abs(obj1[1]-obj2[1])**2 )
    elif len(obj1)==3:
        calc_dist = sqrt( abs(obj1[0]-obj2[0])**2 + abs(obj1[1]-obj2[1])**2 + abs(obj1[2]-obj2[2])**2)
    else:
        raise "Input Must be two or three element float lists."


def find_wp_enu(enu,apparent_radius,heading,look_ahead_dist):
    #finds next waypoint after risk of collision becomes apparent

    for i in range(1,30): #i goes from 1 to 5
        heading_temp=heading-(.088*i)
        x=enu[0]+look_ahead_dist*cos(heading_temp) #heading must be in radians
        y=enu[1]+look_ahead_dist*sin(heading_temp) #heading must be in radians
        enu_look_ahead = [x, y, 0]
        dr_dist=diff_dist(enu_look_ahead,enu) #finding the distance the projected point will be from the object
        if dr_dist > apparent_radius: #if distance to object is greater than safty dist and object radius
            break
        else:
            heading_temp=heading+(.088*i) #checking other direction
            x=enu[0]+look_ahead_dist*cos(heading_temp)
            y=enu[1]+look_ahead_dist*sin(heading_temp)
            enu_look_ahead = [x, y, 0]
            dr_dist=diff_dist(enu_look_ahead,enu)
        if dr_dist > apparent_radius:
            break
    wp=enu_look_ahead
    return wp
