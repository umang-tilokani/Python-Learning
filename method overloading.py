# Method Overloading Alternative Approach
class Addition:
    def sum(self, a=None, b=None, c=None, d=None):
        s = 0
        if a != None and b != None and c != None and d != None:
            s = a + b + c + d
        elif a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


x = Addition()
print(x.sum(32, 51, 3))
