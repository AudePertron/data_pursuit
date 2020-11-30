# -*- coding: utf-8 -*-

import tkinter as tk
import random
from joueur import Joueur
from connect_bdd import Bdd
from traitement_reponse import traitement_reponse
from fonction_question_aléatoire import question_aleatoire
############### Autres fonctions

def j_suivant(dico_joueurs, idj_actuel):
	if idj_actuel == len(dico_joueurs):
		idj_actuel = 1
	else :
		idj_actuel +=1
	return idj_actuel

############### Luigi
	# plus rien 

############### Aude

def traitement_reponse(reponse_joueur, id_question, joueur, theme, difficulte ):    #traitement de la réponse du joueur

    data = Bdd()
    reponse_origine = data.obtenir_reponse_id(id_question) #query qui récupère la bonne réponse 
    reponse_origine = reponse_origine[0][0]   ##reponse_origine[[0,1]]
    print("reponse_origine :", reponse_origine)

    if reponse_joueur == reponse_origine: #si bonne réponse
        #changer par une interface
        print(" ++++++  Réponse correcte")
        print(reponse_origine)
        statut = True       #joueur.tour --> continue à jouer
        if difficulte == 3 : #si question camembert
            fonction_camembert(joueur, theme)    #appeler la fonction de gestion des camemberts. 
    else: 
    	print(" ++++++  Mauvaise réponse ! \n La bonne réponse était :\n", reponse_origine)
    	statut = False      #joueur.tour --> tour suivant

    return statut #booleen True or False pour continuer le tour ou passer au suivant

# PAS ENCORE TESTE !! A VALIDER...
def fonction_camembert(joueur, theme):        
    joueur.camembert.pop(theme)   #valider le camembert de la couleur sélectionnée
    if len(joueur.camembert < 1):
        question_finale()   #si les cinq thèmes sont validés, passer à la question finale
    return joueur

# PAS ENCORE TESTE !! A VALIDER...
# def question_finale(joueur):
#     theme = get_theme_joueur     #récupérer l'input des autres joueurs
#     return theme  #puis repart en jeu "normal"

############### Main

def main():

	# initialisation

	joueur1 = Joueur("Max")
	joueur2 = Joueur("Daniel")
	joueur3 = Joueur("Fernando")
	joueur4 = Joueur("Pierre")

	dico_joueurs = {}
	dico_joueurs[1] = joueur1
	dico_joueurs[2] = joueur2
	dico_joueurs[3] = joueur3
	dico_joueurs[4] = joueur4
	print(dico_joueurs)

	idj_actuel = 1
	stockage = []	

	statut = True
	while statut :
		print(" ++++++++++++++++++++++")
		print(" ++++++  tour en cours :", dico_joueurs[idj_actuel])
		a = question_aleatoire(stockage) #	return aleatoire_question[0], stock_id_question, theme_choisi
		id_question = a[0][0]
		libelle = a[0][1]
		difficulte = a[0][2]
		stockage = a[1]
		theme = a[2]
		print("stockage :\t", stockage)
		print("difficulté :\t", difficulte)
		print("thème :  \t", theme)
		print(" ++++++  Question :", libelle)

		b = input(" ++++++  Votre réponse :")

		statut = traitement_reponse(b, id_question, dico_joueurs[idj_actuel], theme, difficulte)

	idj_actuel = j_suivant(dico_joueurs, idj_actuel)
	print(" ++++++++++++++++++++++")
	print(" ++++++  tour en cours :", dico_joueurs[idj_actuel])

main()



