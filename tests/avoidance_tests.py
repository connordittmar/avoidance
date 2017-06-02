# Unit Tests for avoidance
from bin import gpsutils, types, nav, display
from avoidance import logic
from bin import types

def setup():
    print 'Setup.'

def run():
    print 'Running...'

def test_collision():
    helper = gpsutils.GpsUtils()
    plane_lla = [34.1424319,-38.8124798,100]
    tgt1 = types.Obstacle([34.145151,-38.81298123,0],50)
    check_dist = logic.calc_dist(helper.lla2enu(tgt1.lla,plane_lla))
    print "Distance calculated is %f" % check_dist
    print logic.collision_check(plane_lla,tgt1)



def test_wps():
    plane_lla = [38.977084 , -76.417, 0]
    obj_lla = [38.977084, -76.413, 0]
    wp_lla = [38.977084, -76.407, 0]
    safety_dist = 300
    obj_rad = 100
    look_ahead_dist = 100
    avoider = nav.Avoid(plane_lla,obj_lla,wp_lla,safety_dist,obj_rad,look_ahead_dist)
    wps = avoider.run()
    obstacle_radius = 200
    enu = avoider.get_states(1)
    wp_enu = avoider.get_states(0)
    display.create_plot(wps,enu,obj_rad,obj_rad+safety_dist,wp_enu)

test_wps()
