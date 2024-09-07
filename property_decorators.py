# property decorators allow you to define methods in your class that can be accessed as properties

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def rad(self):
        return self.radius
    

c = Circle(5)
print(c.rad)