# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:05:16 2020

@author: utilisateur
"""
from random import sample

import mysql.connector
import sys

class Bdd:
	@classmethod
	def ouvrir_connexion(cls):
		cls.data = mysql.connector.connect(user ='root', 
			password='root', host='localhost', 
			database='data_pursuit', port='8081')
		cls.curs = cls.data.cursor()

	@classmethod
	def lister_themes(cls):
		cls.ouvrir_connexion()
		cls.curs.execute("SELECT * FROM theme")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient une liste de tuples [(id_theme1, nom_theme1), (id_theme2, nom_theme2), ...]

	@classmethod
	def fermer_connexion(cls):
		cls.curs.close()
		cls.data.close()
        
    @classmethod
	def lister_questions_theme(cls, theme): # on renseigne le thème choisi par l'utilisateur
		cls.ouvrir_connexion()
		cls.curs.execute(f"SELECT id_question, libelle_question, difficulte_question FROM questions WHERE theme_question = {theme}")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient une liste de tuples [(id1, libelle1, diffic1), (id2, libelle2, diffic2), ...] de questions potentielles

	
    def question_aleatoire(lister_themes,lister_questions_theme):
       
       question = []
       liste_question = []
       aleatoire_question = []
       '''
       liste_question_finale = {}
       '''
       #choix aléatoire et affichage des deux thèmes,puis l'utilisateur doit faire un choix
       theme = sample(lister_themes,2)
       print(theme)
       theme = input("Veuillez choisir un theme: ")
       #stockage de tous les id, des libellés et des difficultés des questions du theme sélectionné par le joueur
       for id_question,libelle_question,difficulte_question in (lister_questions_theme):
           question = [(id_question,libelle_question,difficulte_question)]
           liste_question = question + liste_question
 '''   
       #creation d'un dictionnaire 
       for key, value in  liste_question:    
        liste_question_finale.setdefault(key,[]).append(value)
'''
       #choix aléatoire de la question
       aleatoire_question = sample(liste_question,1)
       #recupération des id, et du niveau des questions du theme choisis
       stock_id_question.append(id_question in question_aleatoire())
       #suppression des id_question dejà sélectionnées dans la liste_question
       if id_question in (stock_id_question) and id_question in (liste_question):
           del liste_question[id_question]
       #rajout de toutes les questions supprimées si liste_question est vide 
       if len(liste_question) == 0:
           liste_question = liste_question + stock_id_question
       
       
        
        
        
