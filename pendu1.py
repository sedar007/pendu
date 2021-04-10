#coding : utf-8
from random import choice

from fonctions import *
from liste import *
import os
import pickle
'''
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        
    def whoami (self):
        print("{} a {} points".format(self.nom, self.nom))
'''
'''
p1 = Joueur("Jason")

with open("player.data", "wb") as fic:
    record = pickle.Pickler(fic)
    record.dump(p1) 

with open("player.data", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    player= get_record.load() 
    if "Jason" in Joueur("Jason"):
        print("Deja inscrit")
    else:
        player.whoami()
'''
# On récupère les scores de la partie
scores = recup_scores()

# On récupère un nom d'utilisateur
utilisateur = recup_nom_utilisateur()

# Si l'utilisateur n'a pas encore de score, on l'ajoute
if utilisateur not in scores.keys():
    scores[utilisateur] = 0 # 0 point pour commencer

# Notre variable pour savoir quand arrêter la partie
continuer_partie = 'o'

mot_a_trouver=choix_mot()
mot_trouver=str()

mot_masquer = []

l=len(mot_a_trouver)
i=0


while i<l:
    
    mot_masquer.insert(i,"*")
    
    i=i+1


print("Joueur {0}: {1} point(s)\n".format(utilisateur, scores[utilisateur]))

print("Votre mot contient {} Lettres: \n".format(l))

essais =nb_coups
print("Vous avez {} essais\n".format(essais))
    
while mot_masquer!=mot_a_trouver and essais>0 and essais!=0:
    

    
   
    mot=mot_entrer()
     
    i=0
    while i<l:
        
        
        mot_a_trouver = list(mot_a_trouver)

        if mot==mot_a_trouver[i]:
            
            
            mot_masquer[i]=mot
            mot_trouver=mot_masquer
        i=i+1
        
    mot_trouver=' '.join(mot_masquer)   
    print(mot_trouver)
    
    if mot in mot_a_trouver:

        print("Exellent\n")
    else:
        essais=essais-1
        if essais==0:
            print(" ==========Y= ")
        if essais<=1:
            print(" ||/       |  ")
        if essais<=2:
            print(" ||        0  ")
        if essais<=3:
            print(" ||       /|\ ")
        if essais<=4:
            print(" ||       /|  ")
        if essais<=5:                    
            print("/||           ")
        if essais<=6:
            print("==============\n")

    if not mot_masquer==mot_a_trouver and essais!=0:
        print("Il vous reste {}\n".format(essais))
    
     
if mot_masquer==mot_a_trouver:
    print("Felicitations\n")

else:
    print("Perdu\n")  

scores[utilisateur] += essais 

# La partie est finie, on enregistre les scores
enregistrer_scores(scores)

# On affiche les scores de l'utilisateur
print("Vous finissez la partie avec {0} points.\n".format(scores[utilisateur]))      
            

