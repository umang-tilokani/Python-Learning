# Duck Typing
class Pycharm:
    def execute(self):
        print("Compiling..")
        print("Running..")


class Laptop:
    def code(self, ide):
        ide.execute()


l1 = Laptop()
ide1 = Pycharm()
l1.code(ide1)
