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

    from weapon import Weapon


class Robot:
    def __init__(self,robot_name):
        self.name = 'name'
        self.health = 100
        self.weapon = Weapon()
    
    def attack(self, dinosaur):
        if dinosaur.health >= 0:
            dinosaur.health = dinosaur.health - self.attack_power
            print(f'{self.name} delivers {self.weapon.attack_power} damage to {dinosaur.name}')
            print(f'{dinosaur.name} weakend to {dinosaur.health} health')
        else:
            print("Deafeated!")

class Weapon:
    def __init__(self,):
        self.name = 'rockets'
        self.attack_power = 25

    from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
    def create_herd(self):
        dinosaur1 = Dinosaur('Steg')
        dinosaur2 = Dinosaur('Velo')
        dinosaur3 = Dinosaur('Tea')
        self.dinosaurs.append(dinosaur1)
        self.dinosaurs.append(dinosaur2)
        self.dinosaurs.append(dinosaur3)




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

    
        