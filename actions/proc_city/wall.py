from mcpi.vec3 import Vec3
import random
from .window import Window

class Wall:
    def __init__(self, pos : Vec3, size : Vec3, base=5, bottom_base=None, window_base=5, window_top=None, pane=False, conf=(1, 2), outline=None):
        self.pos = pos
        self.size = size - Vec3(1, 1, 1)
        l = size.x + size.z - 1
        
        if size.x == 1:
            step = Vec3(0,0,1)
        else:
            step = Vec3(1,0,0)
        self.base = base
        self.bottom_base = bottom_base
        # wood (5)
        # log (17)
        # cobble (4)
        # stone (1)
        # glass (20)
        # slab (43)
        
        self.pane = pane
        self.objects = []
        
        # Make windows
        c_conf = [(1, 1)]
        c_weights = [1]
        if (l + 1) % 2 == 0:
            c_conf.append((1, 2))
            c_weights.append(8)
        if (l + 1) % 3 == 0:
            c_conf.append((2, 3))
            c_weights.append(4)
        if (l + 2) % 4 == 0:
            c_conf.append((2, 4))
            c_weights.append(3)
        
        conf = random.choices(c_conf, weights=c_weights)[0]
        
        amount = (l + conf[1] - 1) // conf[1]
        for i in range(amount):
            tsize = step * conf[0] + Vec3(0, size.y, 0)
            tsize.x = max(1, tsize.x)
            tsize.y = max(1, tsize.y)
            tsize.z = max(1, tsize.z)
            self.objects.append(Window(pos + step * conf[1] * i, tsize, bottom=window_base, top=window_top, pane=pane))
        
    def build(self, mc):
        mc.setBlocks(self.pos, self.pos + self.size, self.base)
        if self.bottom_base != None:
            mc.setBlocks(self.pos, self.pos + Vec3(self.size.x, 0, self.size.z), self.bottom_base)
        	
        for obj in self.objects:
            obj.build(mc)
            
    def __repr__(self):
        return f"Window<{self.pos};{self.size}>"
