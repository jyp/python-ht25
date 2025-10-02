import math
class vec3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "vec3(" + str(self.x) +","+str(self.y)+","+str(self.z)+")"
    def add(u,v):
        return vec3(u.x+v.x, u.y+v.y,u.z+v.z)


# an class for vectors in 2d  Euclidean space (no modification allowed so we can share pointers safely)
class vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "vec(" + str(self.x) +","+str(self.y)+")"
    def __add__(self,v):
        return vec(self.x+v.x, self.y+v.y)
    def __sub__(self,v):
        return vec(self.x-v.x, self.y-v.y)
    def scaled(self,s):
        # scalar multiplication
        return vec(s * self.x, s * self.y)
    def __mul__(self,s):
        # scalar multiplication
        return vec(s * self.x, s * self.y)
    def norm(self):
        # the (eucliean) norm of the vector (self)
        return math.sqrt(self.x**2+self.y**2)
    def normed(self):
        # return a vector of the same direction as self, but whose norm is 1
        return self * (1/ self.norm())


u = vec(1,2)
v = vec(3,4)

print(v.normed().norm())

