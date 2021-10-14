

class Dinosaur:
    def __init__(self,dinosaur_name):
        self.name = "name"
        self.health = 100
        self.attack_power = (25)
    
    def attack(self,robot):
        if robot.health >= 0:
            robot.health = robot.health - self.attack_power
            print(f'{self.name} delivers {self.attack_power} damgage to {robot.name}')
            print(f'{robot.name} weakend to {robot.health} health')
        else:
            print('Defeated!')

