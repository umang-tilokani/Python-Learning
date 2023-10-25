# Parameterized Constructor
class Computer:
    def __init__(self, cpu, ram):  # parameterized constructor
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configuration is:", self.cpu, self.ram)


c1 = Computer("M1", "256GB")
c2 = Computer("M2", "512GB")
c1.config()
c2.config()
