# Unit Tests for avoidance
from bin import gpsutils, types, nav, display, nav_multi
from avoidance import logic
from bin import types

def setup():
    print 'Setup.'

def run():
    print 'Running...'

def test_wps():
    plane_lla = [38.977 , -76.417, 0]
    obj_lla = [38.977084, -76.413, 0]
    wp_lla = [38.977084, -76.407, 0]
    safety_dist = 400
    obj_rad = 100
    step_size = 100
    avoider = nav.Avoid(plane_lla,obj_lla,wp_lla,safety_dist,obj_rad,step_size)
    wps = avoider.run()
    enu = avoider.get_states(1)
    wp_enu = avoider.get_states(0)
    display.create_plot(wps,enu,obj_rad,obj_rad+safety_dist,wp_enu)

def test_wps_multi():
    plane_lla = [38.977 , -76.417, 0]
    obj_lla = [[38.977084, -76.413, 0],[38.977084, -76.407, 0]]
    wp_lla = [38.977084, -76.403, 0]
    safety_dist = 400
    obj_rad = 100
    step_size = 100
    obstacles = []
    for i in obj_lla:
        obstacles.append(types.Obstacle(i,obj_rad))
    avoider = nav_multi.Avoid(plane_lla,wp_lla,safety_dist,step_size,obstacles)
    wps = avoider.run()
    obstacles = avoider.get_states(1)
    wp_enu = avoider.get_states(0)
    display.create_plot_multi(wps,obstacles,safety_dist,wp_enu)

test_wps_multi()
