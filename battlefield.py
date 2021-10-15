
from Main import Fleet
from Main import Herd

import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.display_winners(self.battle)()

    
    def display_welcome(self):
        print('Robots vs Dinosaurs')

    
    def battle(self):
        # method to pick robot and dinosaur  
        robots_defeated = False
        dinosaurs_defeated = False
        rotate_count = 1
        while robots_defeated != True and dinosaurs_defeated != True:
            self.robot(random.choice(self.fleet.robots))
            dinosaurs_defeated = self.show_dino_opponent_options()
            self.dinosaur(random.choice(self.herd.dinosaurs))
            robots_defeated = self.show_robo_opponent_options()
            print(f'rotate {rotate_count}')
            rotate_count +=1
        if robots_defeated == True:
            return 'Raawr!'
        if dinosaurs_defeated == True:
            return 'Beep boop, Robots win!'


       
    def dino_turn(self, dinosaur):
        dinosaur.attack(random.choice(self.fleet.robots))

    def robo_turn(self,robot):
        robot.attack(random.choice(self.herd.dinosaurs))
        
    
    def show_dino_opponent_options(self):
        print(f'{self.herd.dinosaurs[0].name} has {self.herd.dinosaurs[0].health}.health')
        print(f'{self.herd.dinosaurs[1].name} has {self.herd.dinosaurs[1].health}.health')
        print(f'{self.herd.dinosaurs[2].name} has {self.herd.dinosaurs[2].health}.health')
        if self.herd.dinosaurs[0].health <= 0 and self.herd.dinosaurs[1].health <= 0 and self.heard.dinosaurs[2].health <= 0:           
            return True
  
    def show_robo_opponent_options(self):
        print(f'{self.fleet.robots[0].name} has {self.fleet.robots[0].health}.health')
        print(f'{self.fleet.robots[1].name} has {self.fleet.robots[1].health}.health')
        print(f'{self.fleet.robots[2].name} has {self.fleet.robots[2].health}.health')
        if self.fleet.robots[0].health <= 0 and self.fleet.robots[1].health <= 0 and self.fleet.robots[2].health <= 0:
            return True

    
    
    def display_winners(self,Win):
        print(Win)