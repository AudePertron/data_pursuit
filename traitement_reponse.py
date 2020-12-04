from joueur import Joueur
from connect_bdd import Bdd
from fonction_question_aléatoire import question_aleatoire
import random

def traitement_reponse(reponse_joueur, id_question, joueur, theme, difficulte, stock ):    #traitement de la réponse du joueur

    reponse_origine= Bdd.obtenir_reponse_id(id_question) #query qui récupère la bonne réponse 
    reponse_origine = reponse_origine[0][0] 
    if reponse_joueur.lower() == reponse_origine.lower(): #si bonne réponse
        
        statut = True       #joueur.tour --> continue à jouer
        if joueur.final == 1:
            print(" Félicitations ! Vous avez gagné!")      #### Changer par l'écran de victoire
            exit #Fin de la partie

        if difficulte == '3' : #si question camembert
            joueur = fonction_camembert(joueur, theme)
            #appeler la fonction de gestion des camemberts. 
    else: 
        statut = False      #joueur.tour --> tour suivant

    return statut, joueur #booleen True or False pour continuer le tour ou passer au suivant


def fonction_camembert(joueur, theme):        
    joueur.camembert.remove(theme)   #valider le camembert de la couleur sélectionnée
    if len(joueur.camembert) < 1:
        joueur.final = 1   #si les cinq thèmes sont validés, passer à la question finale
    return joueur


### séparée des autres fonctions
def question_finale(stock, theme, difficulte):
    themes = Bdd.lister_themes()
    theme = random.sample(themes,1)
    question, stock_id, theme = question_aleatoire(stock, theme, difficulte)
    return question, stock_id, theme