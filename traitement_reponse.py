def traitement_reponse(reponse_joueur, reponse_origine, commentaire, difficulte, joueur, couleur ):    #classe/dictionnaire joueur en input
    if reponse_joueur == reponse_origine: #si bonne réponse
        #changer par une interface
        print("Réponse correcte")
        print(reponse_origine)
        print(commentaire)
        statut = True
        if difficulte = "camembert" : #si question camembert
            fonction_camembert(joueur, couleur)    #appeler la fonction de gestion des camemberts. reflechir à la gestion de la couleur?
        else: 
            ###
            """CODE LUDIVINE"""
            ###

    return statut #booleen true or False pour continuer le tour ou passer au suivant


def fonction_camembert(joueur, couleur):        #joueur serait une classe?
    joueur.camembert.couleur = True   #valider le camembert de la couleur sélectionnée
    for cam in joueur.camembert:
        if cam !=True:
            question_suivante()   #si au moins un camemebrt n'est pas validé, passer à la question suivante
        else:
            question_finale()      #passer à la question finale
# ! Attention, le statut des camemberts du joueur doit être stocké quelque part! return? ou possibité de stocker en classe depuis la fonction?

