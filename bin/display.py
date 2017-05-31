
import sys, os
import pygame
import math

from math import atan2, cos, sin
from pygame.locals import *
from pygame.color import THECOLORS
from types import Vector, Ship, Planet
from physics import Physics


class Display(object):
    def __init__(self):
        pass

    def run(self):
        pygame.init()
        dims = [640,640]
        display_surface = pygame.display.set_mode((dims[0],dims[1]))
        display_surface.fill(THECOLORS["white"])
        gameclock = pygame.time.Clock()
        framerate_limit = 120
        time_s = 0.0
        while not user_done:

            dt_s = float(gameclock.tick( framerate_limit) * 1e-3)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    user_done = True

                elif (event.type == pygame.KEYDOWN):
                    if (event.key == K_ESCAPE):
                        user_done = True
                    elif (event.key==K_w):
                        key_w = 'D'
                    elif (event.key==K_a):
                        key_a = 'D'
                    elif (event.key==K_s):
                        key_s = 'D'
                    elif (event.key==K_d):
                        key_d = 'D'

                elif (event.type == pygame.KEYUP):
                    if (event.key==K_w):
                        key_w = 'U'
                    elif (event.key==K_a):
                        key_a = 'U'
                    elif (event.key==K_s):
                        key_s = 'U'
                    elif (event.key==K_d):
                        key_d = 'U'

            diff.difference(planet.pos,ship.pos)

            if key_w == 'D':
                ship.acc = phys.acceleration(ship.acc,33,ship.dir,diff)
            elif key_s == 'D':
                ship.acc = phys.acceleration(ship.acc,-10,ship.dir,diff)
            else:
                ship.acc = phys.acceleration(ship.acc,0,ship.dir,diff)
            if key_a == 'D':
                ship.dir = ship.dir - 1 * dt_s
            if key_d == 'D':
                ship.dir = ship.dir + 1 * dt_s

            if phys.collision_check(diff,planet.radius):
                boost = phys.acceleration(ship.acc,500,ship.dir,diff)
                if ship.vel.magnitude() == 0 and key_w == 'D':
                    ship.vel = phys.velocity(ship.vel,boost,dt_s)
                else:
                    ship.vel = phys.collision(diff,ship.vel)
            else:
                ship.vel = phys.velocity(ship.vel,ship.acc,dt_s)
            ship.pos = phys.position(ship.pos,ship.vel,dt_s)
            if (ship.pos.x > dims[0]) or (ship.pos.x < 0):
                ship.vel.x = - 1/10 * ship.vel.x
            if (ship.pos.y > dims[1]) or (ship.pos.y < 0):
                ship.vel.y = -1/10 * ship.vel.y
            center = [int( round(ship.pos.x) ), int( round(ship.pos.y) )]
            offset = [center[0]+int(round(10*cos(ship.dir))), center[1]+int(round(10*sin(ship.dir)))]
            rot_img = pygame.transform.rotate(ship_img,-ship.dir*180/3.14159-90)
            display_surface.blit(rot_img,[ship.pos.x-10,ship.pos.y-10])
            #pygame.draw.circle(display_surface, ship.color, center, 10, 1)
            #pygame.draw.circle(display_surface, THECOLORS["blue"], offset, 2,0)
            display_surface.blit(planet_img,[planet.pos.x-planet.radius,planet.pos.y-planet.radius])
            #pygame.draw.circle(display_surface, planet.color, [planet.pos.x,planet.pos.y], planet.radius,1)
            time_s += dt_s

            print time_s,dt_s, gameclock.get_fps()
            pygame.display.flip()
