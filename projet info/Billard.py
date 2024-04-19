import numpy as np
import time

from Billes import *

def dist(bille1,bille2):
    bi
class Billard (list):
    def __init__(self,xmax,ymax,nb_billes):
        self.xmax = xmax
        self.ymax = ymax
        nb_billes += nb_billes%2
        for i in range (nb_billes/2):
            self.append(Bleue(randint(0, xmax), randint(0, ymax)))
            self.append(Rouge(randint(0, xmax), randint(0, ymax)))