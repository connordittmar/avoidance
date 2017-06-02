from bin import gpsutils
from math import sqrt, sin, cos, atan2

def diff_dist(obj1,obj2):
    if len(obj1)==2:
        calc_dist = sqrt( abs(obj1[0]-obj2[0])**2 + abs(obj1[1]-obj2[1])**2 )
        return calc_dist
    elif len(obj1)==3:
        calc_dist = sqrt( abs(obj1[0]-obj2[0])**2 + abs(obj1[1]-obj2[1])**2 + abs(obj1[2]-obj2[2])**2)
        return calc_dist
    else:
        raise "Input Must be two or three element float lists."

def check_for_obstacle(position_of_obstacle,obstacle_radius,point):
    if diff_dist(position_of_obstacle,point) < obstacle_radius:
        return True
    else:
        return False

def find_wp(current_position,position_of_obstacle,obstacle_radius,position_desired,step_size):
    heading = atan2(position_desired[1]-current_position[1],position_desired[0]-current_position[0])
    x = cos(heading)*step_size + current_position[0]
    y = sin(heading)*step_size + current_position[1]
    dr_point = [x, y, 0]

    while(check_for_obstacle(position_of_obstacle,obstacle_radius,dr_point)==True):
        if atan2(position_of_obstacle[1]-current_position[1],position_of_obstacle[0]-current_position[0]) < heading:
            heading += 0.085
            dr_point = [cos(heading)*50+current_position[0], sin(heading)*50+current_position[1], 0]
        else:
            heading -= 0.085
            dr_point = [cos(heading)*50+current_position[0], sin(heading)*50+current_position[1], 0]
    if diff_dist(current_position,position_desired)<step_size:
        dr_point = position_desired
    return dr_point
