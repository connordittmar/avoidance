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

def check_for_danger(obstacles,point=[0,0,0],safety_radius=0):
    for obstacle in obstacles:   #enu coordinates of obstacles
        if check_for_obstacle(obstacle.enu,obstacle.radius+safety_radius,point)==True:
            return True
    return False

def check_for_obstacles(obstacles,dr_point):
    for obstacle in obstacles:
        if check_for_obstacle(obstacle.enu,obstacle.radius,dr_point)==True:
            return obstacle

def find_wp_multi(current_position, obstacles, waypoint, step_size):
    heading = atan2(waypoint[1]-current_position[1],waypoint[0]-current_position[0])
    x = cos(heading)*step_size + current_position[0]
    y = sin(heading)*step_size + current_position[1]
    dr_point = [x, y, 0]
    count = 0
    while(check_for_danger(obstacles,dr_point)==True):
        conflict = check_for_obstacles(obstacles,dr_point)
        dr_point = find_wp(current_position,conflict.enu,conflict.radius,waypoint,step_size)
        count += 1
        if count == 100:
            break
    if diff_dist(current_position,waypoint)<step_size:
        dr_point = waypoint
    return dr_point

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
