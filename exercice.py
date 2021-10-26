#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi


import sys
sys.path.insert(0, "C:\\Users\\bcanu\\OneDrive\\Documents\GitHub\\2021a-c01-ch6-1-exercices-BenCanu")
from exercice_ch6 import frequence

import turtle


# TODO: Définissez vos fonction ici
#Fonction de la question 1

def ellipsoide(a=3, b=5, c=10, masse_volumique=2):
    volume = (4 / 3) * pi * a * b * c
    masse = masse_volumique * volume
    return volume, masse

# Fonction de la question 2
sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"

sorted_lettres = min(sorted(frequence(sentence), key=lambda x: x[0]))

#Fonction de la question 3

def recursive(n):
    if n <= 1:
        return 1
    else:
        return n * recursive(n - 1)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    v, m = ellipsoide()
    print(f"La masse de l'ellipsoïde est de {ellipsoide()[0]:.2f} kilogrammes et son volume est de {ellipsoide()[1]:.2f} litres")


    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(f'Le caractère qui revient le plus souvent est : "{sorted_lettres}"')