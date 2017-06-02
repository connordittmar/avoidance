# Main Loop
from avoidance import logic
from bin import gpsutils
from math import atan2, sin, cos, sqrt
import numpy as np

class Avoid(object):
    def __init__(self,plane_lla,obj_lla,wp_lla,safety_dist,obj_rad,step_size):
        self.plane_lla = plane_lla
        self.obj_lla = obj_lla
        self.wp_lla = wp_lla
        self.safety_dist = safety_dist
        self.obj_rad = obj_rad
        self.helper = gpsutils.GpsUtils()
        self.step_size = step_size

    def run(self):
        helper = self.helper
        plane_lla = self.plane_lla
        obj_lla = self.obj_lla
        wp_lla = self.wp_lla
        safety_dist = self.safety_dist
        obj_rad = self.obj_rad
        step_size = self.step_size

        obstacle_location = helper.lla2enu(obj_lla,plane_lla)
        waypoint_location = helper.lla2enu(wp_lla,plane_lla)
        wp = []
        counter = 0
        sim_location = [0.0,0.0,0.0]
        print obstacle_location
        while(logic.diff_dist(sim_location,obstacle_location)<(safety_dist+obj_rad)):
                wp.append(logic.find_wp(sim_location,obstacle_location,obj_rad,waypoint_location,step_size))
                sim_location = wp[-1]
                if logic.diff_dist(sim_location,obstacle_location)>=(safety_dist+obj_rad):
                    break
                counter +=1
                if counter == 100:
                    break
        return wp

    def get_states(self,into):
        if into == 1:
            enu = self.helper.lla2enu(self.obj_lla,self.plane_lla)
            return enu
        elif into == 0:
            wp_enu = self.helper.lla2enu(self.wp_lla,self.plane_lla)
            return wp_enu
