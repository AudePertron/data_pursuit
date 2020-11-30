from joueur import Joueur
from traitement_reponse import fonction_camembert

joueur1 = Joueur("Stéphanie")
print (joueur1.camembert)

joueur1 = fonction_camembert(joueur1, 3)
print (joueur1.camembert)

joueur1 = Joueur("Max")
joueur2 = Joueur("Daniel")
joueur3 = Joueur("Fernando")
joueur4 = Joueur("Pierre")

dico_joueurs = {}
dico_joueurs[1] = joueur1
dico_joueurs[2] = joueur2
dico_joueurs[3] = joueur3
dico_joueurs[4] = joueur4
print("hello" + str((dico_joueurs[1]).camembert))