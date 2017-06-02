# Main Loop
from avoidance import logic
from bin import gpsutils
from math import atan2, sin, cos, sqrt
import numpy as np

class Avoid(object):
    def __init__(self,plane_lla,obj_lla,wp_lla,safety_dist,obj_rad,look_ahead_dist):
        self.plane_lla = plane_lla
        self.obj_lla = obj_lla
        self.wp_lla = wp_lla
        self.safety_dist = safety_dist
        self.obj_rad = obj_rad
        self.look_ahead_dist = look_ahead_dist
        self.helper = gpsutils.GpsUtils()

    def run(self):
        helper = self.helper
        plane_lla = self.plane_lla
        obj_lla = self.obj_lla
        wp_lla = self.wp_lla
        safety_dist = self.safety_dist
        obj_rad = self.obj_rad
        look_ahead_dist = self.look_ahead_dist

        enu = helper.lla2enu(obj_lla,plane_lla)
        wp_enu = helper.lla2enu(wp_lla,plane_lla)
        heading = atan2(wp_enu[1],wp_enu[0])
        wp = []
        wp_sim_enu = wp_enu
        if logic.collision_check(enu,obj_rad,safety_dist) == True:
            sim_enu = [0.0,0.0,0.0]
            print 'heading',heading * 180.0 / 3.14159
            for i in range(60):
                heading_sim = atan2(wp_sim_enu[1],wp_sim_enu[0])
                look_ahead_enu = [sim_enu[0]+cos(heading_sim)*look_ahead_dist,sim_enu[1]+sin(heading_sim)*look_ahead_dist]
                print "look ahead: ", look_ahead_enu
                if logic.diff_dist(look_ahead_enu,np.subtract(enu,sim_enu)) < (safety_dist + obj_rad):
                    wp.append(logic.find_wp_enu(np.subtract(enu,sim_enu),(obj_rad),heading_sim,look_ahead_dist))
                    print "new waypoint:", wp[i]
                    sim_enu = wp[i]
                else:
                    break
                wp_sim_enu = np.subtract(wp_sim_enu,sim_enu)
        return wp

    def get_states(self,into):
        if into == 1:
            enu = self.helper.lla2enu(self.obj_lla,self.plane_lla)
            return enu
        elif into == 0:
            wp_enu = self.helper.lla2enu(self.wp_lla,self.plane_lla)
            return wp_enu
