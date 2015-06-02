from vector2d import Vector2D
from graphics import egi

class Projectile(object):

    def __init__(self, posx, posy, vel, world=None, radius=5.0):
        self.world = world
        self.radius = radius
        self.pos = Vector2D(posx, posy)
        self.vel = vel

    def render(self):
        egi.aqua_pen()
        egi.circle(self.pos, self.radius)

    def update(self, delta):
        self.pos += self.vel * delta

        # needs to detect collisions
        # if it detects a collision deletes self and increments hits
        # needs to delete itself if off world, increments misses

        if self.pos.distance(self.world.target.pos) <= self.radius + self.world.target.radius:
            self.world.hits += 1
            self.world.projectile = None
            print('hits: ' + str(self.world.hits) + ' misses: ' + str(self.world.misses))

        elif self.pos.x > self.world.cx or self.pos.y > self.world.cy or self.pos.x < 0 or self.pos.y < 0:
            self.world.misses += 1
            self.world.projectile = None
            print('hits: ' + str(self.world.hits) + ' misses: ' + str(self.world.misses))
            