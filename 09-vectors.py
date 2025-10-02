# an class for vectors in 2d  Euclidean space (no modification allowed so we can share)
class vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "vec(" + str(self.x) +","+str(self.y)+")"
    def __add__(self,v):
        return vec(self.x+v.x, self.y+v.y)
    def scaled(self,s):
        return vec(s * self.x, s * self.y)
    def __mul__(self,s):
        return vec(s * self.x, s * self.y)
    # notice we don't want the following:
    # def scale(self,s): 
    #     self.x = s * self.x
    #     self.y = s * self.y

u = vec(1,2)
v = vec(3,4)
# w = vec.add(u,v)
# w = u.__add__(v)

print(u.x)
print(u.__add__)


class vec3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "vec3(" + str(self.x) +","+str(self.y)+","+str(self.z)+")"
    def add(u,v):
        return vec3(u.x+v.x, u.y+v.y,u.z+v.z)

