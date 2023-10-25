# SINGLE INHERITANCE
class rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class square(rectangle):
    def area(self):
        return self.l * self.l


a = rectangle(2, 3)
print("The area of Rectangle is:", a.area())
b = square(2, 3)
print("The area of Square is:", b.area())
