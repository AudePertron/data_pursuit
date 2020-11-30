from joueur import Joueur
from connect_bdd import Bdd

def traitement_reponse(reponse_joueur, id_question, joueur, theme, difficulte ):    #traitement de la réponse du joueur

    reponse_origine= Bdd.obtenir_reponse_id(id_question) #query qui récupère la bonne réponse 
    reponse_origine = reponse_origine[0][0] 
    if reponse_joueur == reponse_origine: #si bonne réponse
        #changer par une interface
        print("Réponse correcte")
        print(reponse_origine)
        statut = True       #joueur.tour --> continue à jouer
        if difficulte == '3' : #si question camembert
            joueur = fonction_camembert(joueur, theme)    #appeler la fonction de gestion des camemberts. 
    else: 
        statut = False      #joueur.tour --> tour suivant

    return statut, joueur #booleen True or False pour continuer le tour ou passer au suivant


def fonction_camembert(joueur, theme):        
    joueur.camembert.remove(theme)   #valider le camembert de la couleur sélectionnée
    if len(joueur.camembert) < 1:
        question_finale()   #si les cinq thèmes sont validés, passer à la question finale
    return joueur

def question_finale(joueur):
    theme = get_theme_joueur     #récupérer l'input des autres joueurs
    return theme  #puis repart en jeu "normal"
