from joueur import Joueur
from coonect_bdd import Bdd

def traitement_reponse(reponse_joueur, id_question, joueur, theme ):    #classe/dictionnaire joueur en input
    reponse_origine = Bdd.obtenir_reponse_id(id_question)
    if reponse_joueur == reponse_origine: #si bonne réponse
        #changer par une interface
        #utiliser query Ludivine pour choper la réponse et difficulté
        print("Réponse correcte")
        print(reponse_origine)
        
        statut = True
        if difficulte = 3 : #si question camembert
            fonction_camembert(joueur, theme)    #appeler la fonction de gestion des camemberts. 
    else: 
        statut = False

    return statut #booleen True or False pour continuer le tour ou passer au suivant


def fonction_camembert(joueur, theme):        
    joueur.camembert.append = theme   #valider le camembert de la couleur sélectionnée
    if len(joueur.camembert >=5):
        question_finale()   #si les cinq thèmes sont validés, passer à la question finale
    return joueur

