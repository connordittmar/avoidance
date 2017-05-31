# Unit Tests for avoidance
from bin import gpsutils
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



test_collision()
