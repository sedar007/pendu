#coding : utf-8
from random import choice

from fonctions import *
from liste import *
import os
import pickle

nom_fichier_scores = "scores"

def choix_mot():
    return choice(liste_mots)

def mot_entrer():


    mot = input("Tapez une lettre: ")
    mot = mot.lower()
    if len(mot)>1 or not mot.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return mot_entrer()

    else:
        return mot

nb_coups = 8




def recup_scores():
    """ récupère les scores enregistrés si le fichier existe.
    """
    
    if os.path.exists(nom_fichier_scores): # Le fichier existe
        # On le récupère
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # Le fichier n'existe pas
        scores = {}
    return scores

def enregistrer_scores(scores):
    """Enregistre les scores dans le fichier
    nom_fichier_scores. """

    fichier_scores = open(nom_fichier_scores, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

# Fonctions gérant les éléments saisis par l'utilisateur

def recup_nom_utilisateur():
    """Fonction chargée de récupérer le nom de l'utilisateur de 4 caractères minimum,
    chiffres et lettres exclusivement.
"""

    nom_utilisateur = input("Tapez votre nom: ")
    # On met la première lettre en majuscule et les autres en minuscules
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur
