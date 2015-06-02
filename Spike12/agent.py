from graphics import egi
from point2d import Point2D
from math import hypot

class Agent(object):

    def __init__(self, world):
        self.world = world
        self.pos = self.world.start._vc.copy()
        self.index = 1

    def update(self):
    	path = self.world.path.path

    	if self.index >= len(path):
    		return

    	dest = self.world.boxes[path[self.index]]._vc.copy()
    	traveldist = hypot(self.pos.x - dest.x, self.pos.y - dest.y)

    	self.pos.x += ((dest.x - self.pos.x)/traveldist) * 5
    	self.pos.y += ((dest.y - self.pos.y)/traveldist) * 5

    	if traveldist < 5:
    		self.index += 1


    def render(self):
    	egi.red_pen()
    	egi.circle(self.pos, 20)