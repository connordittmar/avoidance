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

def check_for_obstacle(position_of_obstacle,obstacle_radius,point=[0,0,0]):
    if diff_dist(position_of_obstacle,point) < obstacle_radius:
        return True
    else:
        return False

def check_for_danger(obstacles):
    for obstacle in obstacles:   #enu coordinates of obstacles
        if check_for_obstacle(obstacle.enu,obstacle.radius)==True:
            return True
    return False

def distance_to_object(dr_point,position_obstacle): #finding closest obstacle to help decide which is most dangerous
    for i in len(position_obstacle):

    return distance_object #used to compare objects and find which is most dangerous

def closing_or_opening_to_object(dr_point,position_obstacle):

    return proximity_change_to_object #2nd part of condition statement to find most dangerous object

def find_dangerous_object(object_distance,)




def find_wp_multi(current_position, position_of_obstacle,obstacle_radius,position_desired,step_size)

    heading = atan2(position_desired[1]-current_position[1],position_desired[0]-current_position[0])
    x = cos(heading)*step_size + current_position[0]
    y = sin(heading)*step_size + current_position[1]
    dr_point = [x, y, 0]




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
