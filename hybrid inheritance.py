# HYBRID INHERITANCE
class figure:
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h


class rectangle(figure):
    def area(self):
        return self.l * self.b


class square(rectangle):
    def area(self):
        return self.l * self.l


class triangle(figure):
    def area(self):
        return (self.b * self.h)/2


a = rectangle(2, 3, 4)
print("The area of Rectangle is:", a.area())
b = square(2, 3, 4)
print("The area of Square is:", b.area())
c = triangle(2, 3, 4)
print("The area of Triangle is:", c.area())
