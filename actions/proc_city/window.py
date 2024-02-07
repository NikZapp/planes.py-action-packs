from mcpi.vec3 import Vec3

class Window:
    def __init__(self, pos : Vec3, size : Vec3, top=None, bottom=None, pane=False):
        self.pos = pos
        self.size = size - Vec3(1, 1, 1)
        self.top = top
        self.bottom = bottom
        self.pane = pane
        
    def build(self, mc):
        mc.setBlocks(self.pos, self.pos + self.size, [20, 102][self.pane])
        if self.bottom != None:
            mc.setBlocks(self.pos, self.pos + self.size - Vec3(0, self.size.y, 0), self.bottom)
        if self.top != None:
            mc.setBlocks(self.pos + Vec3(0, self.size.y, 0), self.pos + self.size, self.top)
        
    def __repr__(self):
        return f"Window<{self.pos};{self.size}>"
