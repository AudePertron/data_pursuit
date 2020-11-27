# -*- coding: utf-8 -*-

import mysql.connector
import sys

class Bdd:

	@classmethod
	def ouvrir_connexion(cls):
		cls.data = mysql.connector.connect(user ='root', 
			password='root', host='localhost', 
			database='trivial', port='8081')
		cls.curs = cls.data.cursor()

	@classmethod
	def fermer_connexion(cls):
		cls.curs.close()
		cls.data.close()

	@classmethod
	def lister_themes(cls):
		cls.ouvrir_connexion()
		cls.curs.execute("SELECT * FROM theme")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient une liste de tuples [(id_theme1, nom_theme1), (id_theme2, nom_theme2), ...]

	@classmethod
	def lister_questions_theme(cls, theme): # on renseigne le thème choisi par l'utilisateur
		cls.ouvrir_connexion()
		cls.curs.execute(f"SELECT id_question, libelle_question, difficulte_question FROM questions WHERE theme_question = {theme}")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient une liste de tuples [(id1, libelle1, diffic1), (id2, libelle2, diffic2), ...] de questions potentielles

	@classmethod
	def obtenir_lib_dif_question(cls, id): # on renseigne l'id (choisi au hasard parmis les id correspondant au thème)
		cls.ouvrir_connexion()
		cls.curs.execute(f"SELECT libelle_question, difficulte_question FROM questions WHERE id_question = {id}")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result  # on obtient un tuple (libelle1, diffic1) qui servira à afficher la question et la difficulté

	@classmethod
	def obtenir_reponse_id(cls, id): # on renseigne l'id de la question qui a été posée à l'utilisateur
		cls.ouvrir_connexion()
		cls.curs.execute(f"SELECT libelle_reponse FROM reponses WHERE id_question = {id} AND valeur_reponse = 1")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient la bonne réponse

	# @classmethod
	# def lister_joueurs(cls):
	# 	cls.ouvrir_connexion()
	#   cls.curs.execute("SELECT nom_joueur FROM joueurs")
	# 	result= cls.curs.fetchall()
	# 	cls.fermer_connexion()
	# 	lj = []
	# 	for joueur in result :
	# 	    lj.append(joueur[0])
	# 	return lj
	
	
# def main():
# 	p = Bdd
# 	l = p.lister_themes()
# 	print(l) #[(1, 'Big Data'), (2, 'IA'), (3, 'Ethique'), (4, 'Python'), (5, 'Mathématique')]
# 	m = p.lister_questions_theme(3)
# 	print(m) # [(1, "Comment appelle-t-on...?", 1), (2, "Quel était le nom ... ?", 2), (3, 'Quelle ... ?', 3)]
# 	n = p.obtenir_lib_dif_question(2)
# 	print(n) # [(2, "Quel était le nom ... ?", 2)]
# 	o = p.obtenir_reponse_id(2)
# 	print(o) # [('Tay',)]

# main()

