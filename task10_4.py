class Sfera:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return 4/3 * 3.14 * self.radius ** 3

    def get_surface_area(self):
        return 4 * 3.14 * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        return (x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2 <= self.radius ** 2


s1 = Sfera()
print(s1.get_volume())
s2 = Sfera(5)
print(s2.get_surface_area())
print(s2.get_center())
s2.set_radius(10)
print(s2.get_radius())
s2.set_center(1, 1, 1)
print(s2.get_center())
print(s2.is_point_inside(9, 9, 9))  
print(s2.is_point_inside(11, 11, 11))