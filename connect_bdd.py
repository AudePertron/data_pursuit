import mysql.connector
import sys

class Bdd:
	def __init__(self):
		self.data = mysql.connector.connect(user ='root', 
			password='root', host='localhost', 
			database='data_pursuit', port='8081')
		self.curs = self.data.cursor()
	self.theme = self.curs.execute("SELECT id_theme FROM theme")
	return self.theme
	

	@classmethod
	def fermer_connexion(cls):
		ls.curs.close()
		cls.data.close()

	@classmethod
	def lister_questions_theme(cls, theme): # on renseigne le thème choisi par l'utilisateur
		cls.curs.execute(f"SELECT id_question, libelle_question, difficulte_question FROM questions WHERE theme_question = {theme}")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient une liste de tuples [(id1, libelle1, diffic1), (id2, libelle2, diffic2), ...] de questions potentielles

    @classmethod
	def obtenir_lib_dif_question(cls, id): # on renseigne l'id (choisi au hasard parmis les id correspondant au thème)
		cls.curs.execute(f"SELECT id_question, libelle_question, difficulte_question FROM questions WHERE id_question = {id}")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result  # on obtient un tuple (id1, libelle1, diffic1) qui servira à afficher la question et la difficulté

	@classmethod
	def obtenir_reponse_id(cls, id): # on renseigne l'id de la question qui a été posée à l'utilisateur
		cls.curs.execute(f"SELECT libelle_reponse FROM reponses WHERE id_question = {id} AND valeur_reponse = 1")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient la bonne réponse

	# @classmethod
	# def lister_joueurs(cls):
	# 	cls.curs.execute("SELECT nom_joueur FROM joueurs")
	# 	result= cls.curs.fetchall()
	# 	cls.fermer_connexion()
	# 	lj = []
	# 	for joueur in result :
	# 	    lj.append(joueur[0])
	# 	return lj


