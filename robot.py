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



        
        