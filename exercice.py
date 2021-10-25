#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from exercice6 import frequence

# TODO: Définissez vos fonction ici
def volume (a,b,c,masse_volumique):
    volume_e = (4/3)* math.pi* a *b *c
    masse = masse_volumique * volume_e
    return volume_e, masse

def lettre_dict ():
    return ...


def valide(adn):
    if len(adn) == 0:
        return False
    else:
        for lettre in adn:   
            if lettre not in ["a", "t", "g", "c"]:
                return False
            else:
                return True
    




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print (volume (2,4,6,10))
    print (valide(input("Entrez votre séquence ")))
    pass
