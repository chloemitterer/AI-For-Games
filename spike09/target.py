from vector2d import Vector2D
from graphics import egi

class Target(object):

    def __init__(self, posx, posy, velx, vely, maxSpeed, world=None, radius=15.0):
        self.world = world
        self.radius = radius
        self.pos = Vector2D(posx, posy)
        self.vel = Vector2D(velx, vely)
        self.maxSpeed = maxSpeed

    def render(self):
        egi.red_pen()
        egi.circle(self.pos, self.radius)

    def update(self, delta):
        self.pos += self.vel * delta
        if self.pos.x < 50:
            self.vel.x = self.maxSpeed
        if self.pos.x > self.world.cx - 50:
            self.vel.x = -self.maxSpeed

        