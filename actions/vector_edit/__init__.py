from mcpi.vec3 import Vec3
from mcpi import minecraft

name = "Vector operations"
# if an app variable exists, it will be set.
app = None

def inc_x():
    vec = app.stack.pop()
    vec.x += 1
    app.stack.push(vec)

def inc_y():
    vec = app.stack.pop()
    vec.y += 1
    app.stack.push(vec)

def inc_z():
    vec = app.stack.pop()
    vec.z += 1
    app.stack.push(vec)

def dec_x():
    vec = app.stack.pop()
    vec.x -= 1
    app.stack.push(vec)

def dec_y():
    vec = app.stack.pop()
    vec.y -= 1
    app.stack.push(vec)

def dec_z():
    vec = app.stack.pop()
    vec.z -= 1
    app.stack.push(vec)


actions = {
    "+x": inc_x,
    "+y": inc_y,
    "+z": inc_z,
    "-x": dec_x,
    "-y": dec_y,
    "-z": dec_z
}
