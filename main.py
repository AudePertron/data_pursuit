# -*- coding: utf-8 -*-

import tkinter as tk
import random
from joueur import Joueur
from connect_bdd import Bdd
from traitement_reponse import traitement_reponse
from traitement_reponse import fonction_camembert	#peut-être pas nécéssaire
from traitement_reponse import question_finale	#idem
from fonction_question_aléatoire import question_aleatoire
############### Autres fonctions

def j_suivant(dico_joueurs, idj_actuel):
	if idj_actuel == len(dico_joueurs):
		idj_actuel = 1
	else :
		idj_actuel +=1
	return idj_actuel


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
	
	
	idj_actuel = 1
	stockage = []
	(dico_joueurs[idj_actuel]).camembert = ['3']
	
#vrai main ?
	statut = True
	while statut :
		print(" ++++++++++++++++++++++")
		print(" ++++++  tour en cours :", dico_joueurs[idj_actuel])
		print("camemberts de base du joueur: " + str((dico_joueurs[idj_actuel]).camembert))
		
		if (dico_joueurs[idj_actuel]).final == 0:
			a = question_aleatoire(stockage,0,0) #	return aleatoire_question[0], stock_id_question, theme_choisi #le zéro sert à laisser le thème en aléatoire
		else:
			a = question_finale(stockage, 0, '3')
		print("test question" +str(a))

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

		statut, joueur = traitement_reponse(b, id_question, dico_joueurs[idj_actuel], theme, '3', stockage)

	idj_actuel = j_suivant(dico_joueurs, idj_actuel)
	print(" ++++++++++++++++++++++")
	print("camemberts après : " + str((dico_joueurs[idj_actuel]).camembert))
	print(" ++++++  tour en cours :", dico_joueurs[idj_actuel])

main()



