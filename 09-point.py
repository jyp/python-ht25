class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Point(" + str(self.x) +","+str(self.y)+")"
    def move(self,dx,dy):
        self.x = self.x +dx
        self.y = self.y +dy

        
p = Point(1,2)
# print(p)
p.move(3,4)
# print(p)

print(bool("a".isdigit))
