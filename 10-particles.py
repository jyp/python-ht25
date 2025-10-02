import random
import math
from graphics import *

G = 150

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


class Particle:
    def __init__(self,pos,vel,mass):
        self.pos = pos
        self.vel = vel
        self.mass = mass
    def newtown_cinematics(self,dt):
        self.pos  = self.pos + self.vel * dt
    def apply_force(self,force,dt):
        acceleration = force * (1 / self.mass)
        self.vel  = self.vel + acceleration * dt

def set_circle_position(c,v):
    currentPos = c.getCenter()
    c.move(v.x-currentPos.getX(),v.y-currentPos.getY()) 

class ParticleView:
    def __init__(self,particle,window):
        self.particle = particle
        self.point = Point(0,0)
        self.circle = Circle(self.point,10)
        self.circle.setFill("magenta")
        self.circle.draw(window)
    def update_view(self):
        set_circle_position(self.circle, self.particle.pos)

# create random particles
particles = []
for i in range(20):
    v = vec(random.uniform(-1,1),random.uniform(-1,1))
    p = vec(random.uniform(-100,100),random.uniform(-100,100))
    m = random.uniform(1,10)
    particles.append(Particle(p,v,m))


# setup window
win = GraphWin("Particle simulation", 640, 480, autoflush=False)
win.setCoords(-320, -240, 320, 240)

# setup views for all particles
particle_views = []
for p in particles:
    particle_views.append(ParticleView(p,win))

######################
# main simulation loop
for i in range(1000000):
    print(i)
    timestep = 0.01
    # simulation on the model
    for p1 in particles:
        for p2 in particles:
            if p1 is not p2:
                r = p1.pos - p2.pos
                g = G * p1.mass * p2.mass / (r.norm()**2)
                d = r.normed()
                f = d * g
                p2.apply_force(f,timestep)
    for p in particles:
        p.newtown_cinematics(timestep)
    # update the view
    for pv in particle_views:
        pv.update_view()
    update(1000)















# timestep = 0.01
# M = 1
# Position in [-100,100]²

# bypass Zelle's graphics interface

