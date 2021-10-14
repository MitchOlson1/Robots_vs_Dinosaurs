from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
    def create_fleet(self):
        robot1 = Robot('tx100')
        robot2 = Robot('tx200')
        robot3 = Robot('tx300')
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
        

        
