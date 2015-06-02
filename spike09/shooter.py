from vector2d import Vector2D
from graphics import egi
from projectile import Projectile
from math import fabs
from random import uniform

class Shooter(object):

    def __init__(self, posx, posy, bulletspeed, world=None, size = 15, accuracy = 0.0):
        self.world = world
        self.size = size
        self.pos = Vector2D(posx, posy)
        self.size = size
        self.aimpos = Vector2D()
        self.bulletspeed = bulletspeed
        self.accuracy = accuracy
        
        

    def shoot(self):
        direction = self.aimpos-self.pos
        direction = direction.normalise()

        offset = Vector2D(uniform(-1, 1), uniform(-1, 1))
        offset = offset * self.accuracy

        direction += offset
                
        self.world.projectile = Projectile(self.pos.x, self.pos.y, direction*self.bulletspeed, self.world)

    def render(self):
        egi.green_pen()
        egi.cross(self.pos, self.size)

        egi.blue_pen()
        egi.cross(self.aimpos, 5)

    def update(self, delta):

        if self.world.target:
            if not self.world.projectile:
                self.aim()
                self.shoot()


    def aim(self):
        ready = False

        time = 1.0
        while not ready:
            self.aimpos = self.world.target.pos + self.world.target.vel * time
            aimdistance = self.aimpos.distance(self.pos)
            bulletdistance = self.bulletspeed * time
            if fabs(aimdistance - bulletdistance) < 0.5:
                ready = True
                print(str(time))
            elif aimdistance > bulletdistance:
                time = time * 1.2
            elif aimdistance < bulletdistance:
                time = time * 0.8

