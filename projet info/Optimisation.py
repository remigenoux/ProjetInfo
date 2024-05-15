# import numpy as np
# import time
# from numpy.random import randint
#
# from Billes import Bille
# from Billard import *


# Ici on va coder les algorithmes permettant d'optimiser le temps de calcul pour modéliser
# la simulation : Par exemple, on va déterminer les collisions possibles à un instant t donné
# en quadrillant le secteur


class Voisins:
    def __init__(self, billes):
        self.billes = billes
        self.list_billes = []
        self.list_voisins = []

    def create_list_billes(self):
        j = 0
        k = 0
        for bille in self.billes:
            if bille.coul() == "Blue":
                j += 1
                self.list_billes.append(f"bille bleue numéro: {j}")
            elif bille.coul() == "Red":
                k += 1
                self.list_billes.append(f"bille rouge numéro: {k}")

    def create_list_voisins(self):
        for i in range(len(self.list_billes)):
            for j in range(i + 1, len(self.list_billes)):
                self.list_voisins.append((self.list_billes[i], self.list_billes[j]))

    def reperage_horizontal(self):
        potential_collisions_horizontal = []
        for i in range(len(self.billes)):
            for j in range(i + 1, len(self.billes)):
                if (self.billes[i].x + self.billes[i].rayon >= self.billes[j].x - self.billes[j].rayon) or \
                        (self.billes[i].x - self.billes[i].rayon <= self.billes[j].x + self.billes[j].rayon):  # les billes sont potentiellement en collision si l'on regarde leurs abscisses
                    potential_collisions_horizontal.append((self.billes[i], self.billes[j]))
        return potential_collisions_horizontal

    def reperage_vertical(self):
        potential_collisions_vertical = []
        for i in range(len(self.billes)):
            for j in range(i + 1, len(self.billes)):
                if (self.billes[i].y + self.billes[i].rayon >= self.billes[j].y - self.billes[j].rayon) or \
                        (self.billes[i].y - self.billes[i].rayon <= self.billes[j].y + self.billes[j].rayon):
                    potential_collisions_vertical.append((self.billes[i], self.billes[j]))
        return potential_collisions_vertical