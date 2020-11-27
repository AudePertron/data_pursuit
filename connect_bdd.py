import mysql.connector
import sys

class Bdd:
    def __init__(self):
        self.data = mysql.connector.connect(user ='root', 
            password='root', host='localhost', 
            database='data_pursuit', port='8081')
        self.curs = self.data.cursor()
	self.curs.execute("SELECT id_theme FROM theme")

    @classmethod
    def fermer_connexion(cls):
    	cls.curs.close()
    	cls.data.close()

    @classmethod
    def obtenir_question(cls, theme):
		cls.curs.execute(f"SELECT id_question, libelle_question, difficulte_question FROM questions WHERE theme_question = {theme}")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result # on obtient une liste de tuples [(id1, libelle1, diffic1), (id2, libelle2, diffic2), ...]

	@classmethod
    def obtenir_reponse_id(cls, id):
		cls.curs.execute(f"SELECT libelle_reponse FROM reponses WHERE id_question = {id} AND valeur_reponse = 1")
		result = cls.curs.fetchall()
		cls.fermer_connexion()
		return result

	@classmethod
    def lister_joueurs(cls):
		cls.curs.execute("SELECT nom_joueur FROM joueurs")
		result= cls.curs.fetchall()
		cls.fermer_connexion()
		lj = []
		for joueur in result :
		    lj.append(joueur[0])
		return lj

