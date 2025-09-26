class Robot:
    def __init__(self, name):
        self.name = name
    def feature(self, feature):
        return "{} does {}".format(self.name, feature)
    def power(self):
        return "{} is Absolute cinema".format(self.name)
robot = Robot("Mecha")
print(robot.feature("Programming"))
print(robot.power())