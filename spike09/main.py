
from graphics import egi, KEY
from pyglet import window, clock
from pyglet.gl import *

from vector2d import Vector2D
from world import World
from target import Target
from shooter import Shooter
from projectile import Projectile

def on_mouse_press(x, y, button, modifiers):
    pass


def on_key_press(symbol, modifiers):
    if symbol == KEY.P:
        world.paused = not world.paused
    if symbol == KEY.R:
        world.shooter = Shooter(50, 50, 700, world, 15, 0.0)
    if symbol == KEY.M:
        world.shooter = Shooter(50, 50, 300, world, 15, 0.0)
    if symbol == KEY.H:
        world.shooter = Shooter(50, 50, 700, world, 15, 0.1)
    if symbol == KEY.G:
        world.shooter = Shooter(50, 50, 300, world, 15, 0.1)


def on_resize(cx, cy):
    world.cx = cx
    world.cy = cy


if __name__ == '__main__':

    # create a pyglet window and set glOptions
    win = window.Window(width=500, height=500, vsync=True, resizable=True)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    # needed so that egi knows where to draw
    egi.InitWithPyglet(win)
    # prep the fps display
    fps_display = clock.ClockDisplay()
    # register key and mouse event handlers
    win.push_handlers(on_key_press)
    win.push_handlers(on_mouse_press)
    win.push_handlers(on_resize)

    # create a world 
    world = World(500, 500)
    world.target=Target(450, 450, 100, 0, 100, world, 15)
    world.shooter = Shooter(50, 50, 700, world, 15)

    world.paused = False

    while not win.has_exit:
        win.dispatch_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # show nice FPS bottom right (default)
        delta = clock.tick()
        world.update(delta)
        world.render()
        fps_display.draw()
        # swap the double buffer
        win.flip()

