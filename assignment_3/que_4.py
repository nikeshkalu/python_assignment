import math
class circle:
    def __init__(self,radius):
        self.radius = radius

    def calArea(self):
        return math.pi*(self.radius^2)

    @property
    def getRadius(self):
        return self.radius

    @getRadius.setter
    def getRadius(self, radius):
        self.radius = radius


a = circle(radius=10)
print(a.calArea())

a.getRadius = 20
print(a.calArea())
