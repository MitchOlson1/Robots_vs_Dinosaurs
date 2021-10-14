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
