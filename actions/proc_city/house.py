from mcpi.vec3 import Vec3
from .outline import Outline
from .wall import Wall

class House:
    def __init__(self, p0 : Vec3, p1 : Vec3):
        self.pos = Vec3(min(p0.x, p1.x), min(p0.y, p1.y), min(p0.z, p1.z))
        self.size = Vec3(max(p0.x, p1.x), max(p0.y, p1.y), max(p0.z, p1.z)) - self.pos
        self.objects = []
        self.objects.append(Outline(p0, p1, 35, 3))
        self.objects.append(Wall(p0 + Vec3(1, 1, 0), self.size - Vec3(1, 1, -1) - Vec3(0, 0, self.size.z)))
        self.objects.append(Wall(p0 + Vec3(1, 1, self.size.z), self.size - Vec3(1, 1, -1) - Vec3(0, 0, self.size.z)))
        self.objects.append(Wall(p0 + Vec3(0, 1, 1), self.size - Vec3(-1, 1, 1) - Vec3(self.size.x, 0, 0)))
        self.objects.append(Wall(p0 + Vec3(self.size.x, 1, 1), self.size - Vec3(-1, 1, 1) - Vec3(self.size.x, 0, 0)))

    def build(self, mc):
        for obj in self.objects:
            obj.build(mc)

    def __repr__(self):
        return f"House<{self.pos};{self.size}>"
