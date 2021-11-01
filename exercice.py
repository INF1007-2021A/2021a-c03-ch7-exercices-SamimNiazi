#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from exercice6 import frequence
from turtle import *
# TODO: Définissez vos fonction ici
def volume (a=0,b=0,c=0,masse_volumique=0):
    volume_e = (4/3)* math.pi* a *b *c
    masse = masse_volumique * volume_e
    return volume_e, masse




def valide(adn):
    if len(adn) == 0:
        return False
    else:
        for lettre in adn:   
            if lettre not in ["a", "t", "g", "c","A","T","G","C"]:
                return False
            else:
                return True
def saise (type):
    value = input(f"Entrez {type}")
    if valide(value) is True:
        return value
    else:
        print ("le type n'est pas accepter")

def proportion(chaine, sequence):
    chaine.replace(" ",'')
    sequence.replace(" ",'')
    nb_doccurence = sequence.count(chaine)
    proportions = (nb_doccurence / (len(sequence)))* 100
   
    return ("La proportion est de :" , proportions, " %")
    




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print (volume (2,4,6,10))
    print (valide(input("Entrez votre séquence ")))
    print (proportion(input("entrer un chaine de d'adn "),input("entrer une sequence d'adn ") ))
    pass
