# Main Loop
from avoidance import logic
from bin import gpsutils
from math import atan2, sin, cos, sqrt
import numpy as np

class Avoid(object):
    def __init__(self,plane_lla,wp_lla,safety_dist,step_size,obstacles):
        self.plane_lla = plane_lla
        self.wp_lla = wp_lla
        self.safety_dist = safety_dist
        self.helper = gpsutils.GpsUtils()
        self.step_size = step_size
        self.obstacles = obstacles
    def run(self):
        helper = self.helper
        plane_lla = self.plane_lla
        wp_lla = self.wp_lla
        safety_dist = self.safety_dist
        step_size = self.step_size
        obstacles = self.obstacles

        for elem in obstacles:
            elem.enu = helper.lla2enu(elem.lla,plane_lla)
        print "running..."
        if logic.check_for_danger(obstacles,[0,0,0],safety_dist):
            waypoint_location = helper.lla2enu(wp_lla,plane_lla)
            wp = []
            print "MADE IT ......"
            sim_location = [0.0,0.0,0.0]
            count = 0
            while(logic.check_for_danger(obstacles,sim_location,safety_dist)):
                    wp.append(logic.find_wp_multi(sim_location,obstacles,waypoint_location,step_size))
                    sim_location = wp[-1]
                    count += 1
                    if count == 100:
                        break
            return wp

    def get_states(self,into):
        if into == 1:
            obstacles = self.obstacles
            return obstacles
        elif into == 0:
            wp_enu = self.helper.lla2enu(self.wp_lla,self.plane_lla)
            return wp_enu
