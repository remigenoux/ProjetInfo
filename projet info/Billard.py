import numpy as np
import time
from numpy.random import randint


from Billes import *
def dist(u,v):
    return np.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)

class Billard (list):
    def __init__(self,xmax,ymax,nb_billes,dt):
        self.xmax = xmax
        self.ymax = ymax
        self.dt = dt
        nb_billes += nb_billes%2
        self.append(Blanche(xmax//2,ymax//2))
        r= Bille.taille
        while len(self)<=(nb_billes/2):
            x1,y1 = randint(0+r, xmax-r), randint(0+r, ymax-r )
            Plein=False
            for j in range (len(self)):
                if dist(self[j].coords,(x1,y1))<r :
                    Plein = True
            if not Plein :
                self.append(Bleue(x1,y1))
        while len(self) <= (nb_billes):
            x2,y2 = randint(0+r, xmax-r ), randint(0+r, ymax-r)
            Plein = False
            for j in range(len(self)):
                if dist(self[j], (x2,y2)) < r:
                    Plein = True
            if not Plein:
                self.append(Rouge(x2, y2))
    def UnTour(self,J):
        force = input("veuillez entrer une vitesse")
        x = input("veuillez entrer une direction x")
        y = input ("veuillez entrer une direction y")
        try :
            force = int(force)
            direction = (int(x),int(y))
        except ValueError:
            print("Vous n'avez pas répondu correctement aux questions")

        if J == 'IA' :
            Blanche.attribut = 'Rouge' #   on attribue la sous couleur "bleue ou rouge"
        else :
            Blanche.attribut = J
        mouvement = []                      #IL FAUT METTRE LA BLANCHE DEDANS
        while len(mouvement)!= 0 :
            simulation()
        #   on met la boule blanche dans la liste mouvement
        #   tant que au moins une bille est en mouvement : simulation()
        #   on change les positions dans Billard

    def simulation(self):
        # on étudie les positions de toutes les billes en mouvement (liste) après ce pas de temps
        # on établit les potentiels contacts
        # on établit le temps des contacts
        # on gère le contacts avec les fonctions qu'on connaît déjà
        # on avance toute la simulation du temps
        # on
        return 0


    def partie(self):
        nbr = input("Voulez-vous jouer contre un ami ? (1=oui,2=non)")
        try:
            Joueur = int(nbr)
        except ValueError:
            print("Vous n'avez pas répondu correctement à la question")
        tour=1
        J = 'Bleu'
        while not self.fin_partie():
            print("c'est le tour",tour,"c'est à ",J,"de jouer")
            self.UnTour(J)
            if Joueur == 1 :
                if J == 'Bleu':
                    J='Rouge'
                else :
                    J = 'Bleu'
            elif Joueur == 2 :
                if J == 'Bleu':
                    J='IA'
                else :
                    J = 'Bleu'
            tour+=1





