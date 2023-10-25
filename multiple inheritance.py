# MULTIPLE INHERITANCE
class room:
    l = 0
    b = 0
    h = 0

    def area(self):
        return 2 * ((self.l * self.b) + (self.b * self.h) + (self.l * self.h))


class paint:
    cost = 0

    def paintcost(self):
        return self.cost


class bill(room, paint):
    def paintingcost(self):
        print("The cost to paint a room with area ", (2 * ((self.l * self.b) + (self.b * self.h) + (self.l * self.h))),
              " and the cost of paint ", str(self.cost), " is ",
              (2 * ((self.l * self.b) + (self.b * self.h) + (self.l * self.h))) * self.cost, ".")


a = bill()
a.l = int(input("Enter the length of room: "))
a.b = int(input("Enter the breadth of room: "))
a.h = int(input("Enter the height of room: "))
a.cost = int(input("Enter the cost of paint: "))
a.paintingcost()
