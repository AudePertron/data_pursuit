import tkinter as tk
from tkinter import ttk

#utilisation de Tkinter pour interface graphique page acceuil Trivial Pursuit IA
# Création de la fenêtre de l'application
root = tk.Tk()
# Définir un titre pour la fenêtre
root.title("TRIVIAL PURSUIT IA")
# Définir la taille de la fenêtre 
root.geometry("400x400") # mettre les pixels suivant ce pattern 0pixels x 0pixels
# Définir la couleur du fond
root.configure(bg="cyan") # bg = background

# Définir une taille minimale
root.minsize(600, 600)
# Définir une taille maximale
root.maxsize(800, 800)


# Création d'une frame qui contiendra les titres
frame_titre = tk.Frame(root, bg="blue") # root est la fenêtre à laquelle la frame est rattachée

# Permet de l'insérer dans la fenêtre
frame_titre.pack()

# On définit le texte que l'on veut afficher dans notre frame
titre = tk.Label(frame_titre, text='Bienvenue sur TRIVIAL PURSUIT IA !!!!', font=("Helvetica", "30"), bg='blue', fg='black')
# text = le texte à afficher, font = définir une police particulière et sa taille, 
# bg = couleur de l'arrière plan, et fg = couleur du texte

# Il faut également lui dire de l'afficher dans la frame
titre.pack(pady=50, padx=50) 
# pady et padx sont des marges en pixels sur les axes y et x, 
# c'est-à-dire en vertical et en horizontal respectivement.
# Ces marges nous permettront de voir la couleur de la frame qui comprend notre texte.


#Nombre de participant
#label nombre de participant

labelchoix = tk.Label(root, text='Veuillez choisir un nombre de joueurs', font=("Helvetica", 20), bg='orange', fg='white')
labelchoix.pack(pady=10, padx=10)
#labelchoix.place(x=5, y=50) 


# Afficher l'entry dans la fenêtre
#saisie_nb_joueurs.pack(pady=10, padx=10)

#création d'une liste déroulante pour le nombre de joueurs
nb_joueurs=[1,2,3,4]
listecombo = ttk.Combobox(root, values=nb_joueurs)
#choisi l'élément qui s'affiche par défaut à savoir 1 joueur
listecombo.current(0)
listecombo.pack(pady=10, padx=10)

#label de chaque joueurs
labeljoueur1 = tk.Label(root, text='joueur1', font=("Helvetica", 12), bg='orange', fg='white')
#labelchoix.pack(pady=10, padx=10) 
labeljoueur1.place(x=5, y=300)
labeljoueur2 = tk.Label(root, text='joueur2', font=("Helvetica", 12), bg='orange', fg='white')
labeljoueur2.place(x=5, y=350)
labeljoueur3 = tk.Label(root, text='joueur3', font=("Helvetica", 12), bg='orange', fg='white')
labeljoueur3.place(x=5, y=400)
labeljoueur4 = tk.Label(root, text='joueur4', font=("Helvetica", 12), bg='orange', fg='white')
labeljoueur4.place(x=5, y=450)


#Zone de saisie des joueurs
saisie_joueur1 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 12), bg="Blue", fg="black")
# justify = permet de définir comment le texte est justifié, soit "center", "left", "right"
# par défaut le texte est justifié à gauche
# Afficher l'entry dans la fenêtre
saisie_joueur1.place(x=150, y=300)
saisie_joueur2 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 12), bg="blue", fg="black")
saisie_joueur2.place(x=150, y=350)
saisie_joueur3 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 12), bg="blue", fg="black")
saisie_joueur3.place(x=150, y=400)
saisie_joueur4 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 12), bg="blue", fg="black")
saisie_joueur4.place(x=150, y=450)


#création bouton entrez dans le jeu
#action du bouton qui permet de passer à la page d'interface suivante
#def entrer():
    


# Création du bouton
#bouton = tk.Button(root, text='ENTRER DANS LE JEU', height=5, width=20, bd=0, bg='orange', fg='black')
# height = permet de définir la hauteur du bouton, width = définir la largeur, 
# bd = pour lui dire que l'on veut un bouton sans bordure,
# command = permet de lui indiquer une fonction a exécuter lorsque l'utilisateur clique sur le bouton

# Il est possible de modifier les propriétés d'un bouton pour lui ajouter une commande
#bouton.configure(command=entrer) # la fonction appelée ne prend pas d'arguments donc pas de ()

# Afficher le bouton dans la frame
#bouton.pack()













root.mainloop()
