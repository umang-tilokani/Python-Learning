# Method Overriding
# Same name method, with same parameter list in different classes
class A:
    def show(self):
        print("in a")


class B(A):
    def show(self):
        print("in b")


b = B()
b.show()
