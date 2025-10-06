import math

def identity(x):
    return x

# example types:
print(1234, type(1234))
print(1234.0, type(1234.0))
print(math.pi, type(math.pi))
print(identity, type(identity))
print(int, type(int))
print([1,2,3], type([1,2,3]))
print((1,2,3), type((1,2,3)))


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
    def __lt__(self,other):
        return self.norm() < other.norm()

u = vec(1,2)
v = vec(3,4)

print(u.__add__(v))
###################
print("my_sum examples")
def my_sum(list):
    result = list[0]
    for x in list[1:]:
        result = result + x
    return result

print(my_sum([1,5,3,4]))
print(my_sum([u,v,v,vec(23,45)]))

###################
print("sort examples")
print(sorted([2,1,5,4,6]))
print(sorted(["world","hello"]))
print(sorted([u,v]))
 #  ^ note that the typechecker sees that this is ok or not depending on existence of __lt__ method

################
## Static checking examples

# x : int
# x = 456.0

def make_greeting(name: str) -> str:
    return ("hello" + name)

def greeting(name: str) -> None:
    print(make_greeting (name))

greeting("John")
# greeting(1234) # detected as an error without running the program!

print(sorted([u,v]))

############
##
print("pop example. ")
example_list = [3,4,5,6]
print("example_list before", example_list)
print("popped", list.pop(example_list))
print("example_list after", example_list)
