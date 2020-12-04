from joueur import Joueur
from connect_bdd import Bdd
from fonction_question_aléatoire import question_aleatoire
import random
from PyQt5 import QtCore, QtGui, QtWidgets

def traitement_reponse(reponse_joueur, id_question, joueur, theme, difficulte, stock ):    #traitement de la réponse du joueur

    reponse_origine= Bdd.obtenir_reponse_id(id_question) #query qui récupère la bonne réponse 
    reponse_origine = reponse_origine[0][0] 
    
    if reponse_joueur.lower() == reponse_origine.lower(): #si bonne réponse
        
        statut = True       #joueur.tour --> continue à jouer
        if joueur.final == 1:
            print(" Félicitations ! Vous avez gagné!")      #### Changer par l'écran de victoire
            #QMessageBox.about(self, "Victoire! ", "Félicitations ! Vous avez gagné!")
            exit #Fin de la partie

        if difficulte == 3 : #si question camembert
            joueur = fonction_camembert(joueur, theme)
            #appeler la fonction de gestion des camemberts. 
    else: 
        statut = False      #joueur.tour --> tour suivant

    return statut, joueur #booleen True or False pour continuer le tour ou passer au suivant


def fonction_camembert(joueur, theme):        
    # dico_camembert = { 
    #             1 : { 
    #                 1 : "cam_1_1" , 2 : "cam_1_2" , 3 : "cam_1_3" , 4 : "cam_1_4", 5 : "cam_1_5"} , 
    #             2 : {
    #                 1 : "cam_2_1" , 2 : "cam_2_2" , 3 : "cam_2_3" , 4 : "cam_2_4", 5 : "cam_2_5"} ,
    #             3 : {
    #                 1 : "cam_3_1" , 2 : "cam_3_2" , 3 : "cam_3_3" , 4 : "cam_3_4", 5 : "cam_3_5"} ,
    #             4 : { 
    #                 1 : "cam_4_1" , 2 : "cam_4_2" , 3 : "cam_4_3" , 4 : "cam_4_4", 5 : "cam_4_5"} , 
    #             5 : { 
    #                 1 : "cam_5_1" , 2 : "cam_5_2" , 3 : "cam_5_3" , 4 : "cam_5_4", 5 : "cam_5_5"} 
    #                 }
    
    # setcouleur = dico_camembert[joueur][theme]
    # print(setcouleur)
    # self.Ui_MainWindow.setcouleur.setEnabled(True)
    if theme in joueur.camembert:
        joueur.camembert.remove(theme)   #valider le camembert de la couleur sélectionnée
    print(joueur.camembert)
    if len(joueur.camembert) < 1:
        joueur.final = 1   #si les cinq thèmes sont validés, passer à la question finale
    return joueur

### séparée des autres fonctions
def question_finale(stock, theme, difficulte):
    themes = Bdd.lister_themes()
    theme = random.sample(themes,1)
    question, stock_id, theme = question_aleatoire(stock, theme, difficulte)
    return question, stock_id, theme

