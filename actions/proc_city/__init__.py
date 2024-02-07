name = "Procedural"
app = None

import time
from mcpi.vec3 import Vec3
from . import wall
from . import house
import random

seed = 12345

def make_wall():
    global seed
    random.seed(seed)
    params = {
        'base' : random.choice([5, 17, 4, 1, 43]),
        'bottom_base' : random.choice([5, 17, 4, 1, 43, None, None, None, None, None, None]),
        'window_base' : random.choice([5, 17, 4, 1, 43]),
        'window_top' : random.choice([5, 17, 4, 1, 43, None, None, None, None]),
        'pane' : random.choice([True, False, False])
    }
    pos1, pos2 = app.stack.pop(2)
    origin = Vec3(min(pos1.x, pos2.x), min(pos1.y, pos2.y), min(pos1.z, pos2.z))
    end = Vec3(max(pos1.x, pos2.x), max(pos1.y, pos2.y), max(pos1.z, pos2.z))
    size = end - origin + Vec3(1, 1, 1)
    w = wall.Wall(origin, size, **params)
    w.build(app.mcpi.mc)

def set_seed():
    global seed
    key = app.stack.pop()
    seed = key.x * key.y + key.x * key.x * key.z + key.z - key.y
    print(seed)

actions = {
    "Set seed" : set_seed,
    "Build wall" : make_wall
}
