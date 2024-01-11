class Circle:
    _pi = 3.14

    def __init__(self, diameter=0):
        self.diameter = diameter
        self.radius = diameter / 2

    def circumference(self):
        return Circle._pi * self.diameter

    def area(self):
        return Circle._pi * self.radius ** 2

    def area_sector(self, angle):
        return Circle._pi * (self.radius ** 2) * (angle / 360)
