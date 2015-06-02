'''A 2d world that supports agents with steering behaviour

Created for COS30002 AI for Games by Clinton Woodward cwoodward@swin.edu.au

'''

from vector2d import Vector2D
from matrix33 import Matrix33
from graphics import egi


class World(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        
        self.shooter = None
        self.target = None
        self.projectile = None

        self.hits = 0
        self.misses = 0

        self.paused = True




    def update(self, delta):
        if not self.paused:
            if self.shooter:
                self.shooter.update(delta)
            if self.target:
                self.target.update(delta)
            if self.projectile:
                self.projectile.update(delta)

    def render(self):
        if self.shooter:
            self.shooter.render()
        if self.target:
            self.target.render()
        if self.projectile:
            self.projectile.render()


    def transform_points(self, points, pos, forward, side, scale):
        ''' Transform the given list of points, using the provided position,
            direction and scale, to object world space. '''
        # make a copy of original points (so we don't trash them)
        wld_pts = [pt.copy() for pt in points]
        # create a transformation matrix to perform the operations
        mat = Matrix33()
        # scale,
        mat.scale_update(scale.x, scale.y)
        # rotate
        mat.rotate_by_vectors_update(forward, side)
        # and translate
        mat.translate_update(pos.x, pos.y)
        # now transform all the points (vertices)
        mat.transform_vector2d_list(wld_pts)
        # done
        return wld_pts
    def transform_point(self, point, pos, forward, side):
        ''' Transform the given single point, using the provided position,
            and direction (forward and side unit vectors), to object world space. '''
        # make a copy of the original point (so we don't trash it)
        wld_pt = point.copy()
        # create a transformation matrix to perform the operations
        mat = Matrix33()
        # rotate
        mat.rotate_by_vectors_update(forward, side)
        # and translate
        mat.translate_update(pos.x, pos.y)
        # now transform the point (in place)
        mat.transform_vector2d(wld_pt)
        # done
        return wld_pt