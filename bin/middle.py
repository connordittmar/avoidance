from avoidance import logic
from math import sin, cos, atan2
location = [0,0]
obstacle_radius = 10
obstacle_location = [15,0]
goal_location = [30,0]

def find_wp(location,obstacle_location,obstacle_radius,goal_location):
    heading = atan2(goal_location[1],goal_location[0])
    waypoint = [ location[0] + cos(heading)*20, location[1] + sin(heading)*20]
    counter = 0
    while(logic.diff_dist(waypoint,obstacle_location)<obstacle_radius):
        print "diff dist = ", logic.diff_dist(waypoint,obstacle_location)
        heading -= 0.08
        waypoint = [ location[0] + cos(heading)*20, location[1] + sin(heading)*20]
        print waypoint
        counter +=1
        if counter == 100:
            break
    print "final waypoint"
find_wp(location,obstacle_location,obstacle_radius,goal_location)
