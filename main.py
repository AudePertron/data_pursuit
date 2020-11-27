# -*- coding: utf-8 -*-



# pour l'instant le main contient les parties de Aude et Luigi, pour le test... 
# je n'y ai pas touché depuis vendredi après-midi... amusez vous bien !
# si vous travaillez dessus ce weekend, pensez à bien créer des "Branch"

import tkinter as tk
from joueur import Joueur
from connect_bdd import Bdd
import random

data = Bdd()

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
print("tour en cours :", dico_joueurs[idj_actuel])

def j_suivant(idj_actuel):
	if idj_actuel == len(dico_joueurs):
		idj_actuel = 1
	else :
		idj_actuel +=1
	return idj_actuel

idj_actuel = j_suivant(idj_actuel)
print("tour en cours :", dico_joueurs[idj_actuel])


###############
stockage = []

def question_aleatoire(stock):
   
	# question = []
	# liste_question = []
	aleatoire_question = []
	stock_id_question = stock

    #liste_question_finale = {}
    #choix aléatoire et affichage des deux thèmes,puis l'utilisateur doit faire un choix
	themes = data.lister_themes()

	themes_au_choix = random.sample(themes,2)
	print(themes_au_choix)
	theme_choisi = input("Veuillez choisir un theme: ")
    #stockage de tous les id, des libellés et des difficultés des questions du theme sélectionné par le joueur 

	liste_question = data.lister_questions_theme(theme_choisi)


    #creation d'un dictionnaire 

    #choix aléatoire de la question
	aleatoire_question = random.sample(liste_question,1)
	while aleatoire_question[0][0] in stock_id_question : # [(5, 'ksjfle', 3), (6, 'isjape', 3)]
		aleatoire_question = random.sample(liste_question,1)

    #recupération des id, et du niveau des questions du theme choisis
    	# stock_id_question.append(id_question in question_aleatoire
	id_question = aleatoire_question[0][0]
	stock_id_question.append(id_question)
    #suppression des id_question dejà sélectionnées dans la liste_question
		# if id_question in (stock_id_question) and id_question in (liste_question):
		# 	del liste_question[id_question]
    #rajout de toutes les questions supprimées si liste_question est vide 
	if len(liste_question) == 0:
		# 	liste_question = liste_question + stock_id_question
		stock_id_question = []

	return aleatoire_question[0], stock_id_question



def traitement_reponse(reponse_joueur, id_question, joueur, theme, difficulte ):    #traitement de la réponse du joueur

    reponse_origine= Bdd.obtenir_reponse_id(id_question) #query qui récupère la bonne réponse 

    if reponse_joueur == reponse_origine: #si bonne réponse
        #changer par une interface
        print("Réponse correcte")
        print(reponse_origine)
        statut = True       #joueur.tour --> continue à jouer
        if difficulte == 3 : #si question camembert
            fonction_camembert(joueur, theme)    #appeler la fonction de gestion des camemberts. 
    else: 
        statut = False      #joueur.tour --> tour suivant

    return statut #booleen True or False pour continuer le tour ou passer au suivant


def fonction_camembert(joueur, theme):        
    joueur.camembert.pop(theme)   #valider le camembert de la couleur sélectionnée
    if len(joueur.camembert < 1):
        question_finale()   #si les cinq thèmes sont validés, passer à la question finale
    return joueur

def question_finale(joueur):
    theme = get_theme_joueur     #récupérer l'input des autres joueurs
    return theme  #puis repart en jeu "normal"


a = question_aleatoire(stockage)
id_question = a[0][0]
libelle = a[0][1]
difficulte = a[0][2]
stockage = a[1]
print(stockage)
print(libelle)

b = input("votre réponse :")

traitement_reponse(b, id_question, dico_joueurs[idj_actuel], 3, difficulte)

idj_actuel = j_suivant(idj_actuel)
print("tour en cours :", dico_joueurs[idj_actuel])




# questions = [(1, 'blabla', 2), (2, 'blublu', 2), (3, 'blablabla', 1), (4, 'bla', 3)]
   
   

