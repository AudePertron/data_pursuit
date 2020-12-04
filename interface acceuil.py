#import Image
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
root.configure(bg="#55557f") # bg = background

# Définir une taille minimale
root.minsize(600, 600)
# Définir une taille maximale
root.maxsize(1500, 1500)


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

labelchoix = tk.Label(root, text='Veuillez choisir un nombre de joueurs', font=("Helvetica", 20), bd=10, bg='orange', fg='white')
labelchoix.pack(pady=10, padx=10)
#labelchoix.place(x=5, y=50) 


# Afficher l'entry dans la fenêtre
#saisie_nb_joueurs.pack(pady=10, padx=10)

#création d'une liste déroulante pour le nombre de joueurs
#création d'une fonction pour griser les champs de saisie en fonction du nombre de joueurs sélectionnés.
def update(i):
    nb_joueurs = int(listecombo.get()) #on récupère la valeur entrée pour le nombre de joueurs
    if nb_joueurs ==2:
        saisie_joueur2.configure(state=tk.NORMAL) # pour 2 joueurs on ne grise que les joueurs 3 et 4
    elif nb_joueurs ==3:
        saisie_joueur2.configure(state=tk.NORMAL) # pour 3 joueurs on ne grise que le joueur 4
        saisie_joueur3.configure(state=tk.NORMAL)
    elif nb_joueurs ==4:
        saisie_joueur2.configure(state=tk.NORMAL) # pour 4 joueurs on ne grise rien
        saisie_joueur3.configure(state=tk.NORMAL)
        saisie_joueur4.configure(state=tk.NORMAL)
 
nb_joueurs=[1,2,3,4]
listecombo = ttk.Combobox(root, values=nb_joueurs)
listecombo.bind('<<ComboboxSelected>>', update)
#choisi l'élément qui s'affiche par défaut à savoir 1 joueur
listecombo.current(0)
listecombo.pack(pady=10, padx=10)

#label de chaque joueurs
labeljoueur1 = tk.Label(root, text='joueur1', font=("Helvetica", 12), bg='orange', fg='white')
labeljoueur1.place(x=5, y=300)
labeljoueur2 = tk.Label(root, text='joueur2', font=("Helvetica", 12), bg='orange', fg='white')
labeljoueur2.place(x=5, y=350)
labeljoueur3 = tk.Label(root, text='joueur3', font=("Helvetica", 12), bg='orange', fg='white')
labeljoueur3.place(x=5, y=400)
labeljoueur4 = tk.Label(root, text='joueur4', font=("Helvetica", 12), bg='orange', fg='white')
labeljoueur4.place(x=5, y=450)

#récupérarion des saisie de noms
def recup():
    listenom=[]
    nom1=saisie_joueur1.get()
    nom2=saisie_joueur2.get()
    nom3=saisie_joueur3.get()
    nom4=saisie_joueur4.get()
    
    
    print(nom1)
    listenom.append([nom1, nom2, nom3, nom4])
    print(listenom)

boutonvalider = tk.Button(root, text='Valider les joueurs', font=("Helvetica", 14), height=3, width=15, bd=10, bg='orange', fg='Black', command=recup)
# Afficher le bouton dans la frame
boutonvalider.place(x=700, y=500)

#Zone de saisie des joueurs
# Cas initial : On a un joueur par défaut
saisie_joueur1 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 14), bg="Blue", fg="white")
saisie_joueur1.place(x=150, y=300)
saisie_joueur2 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 14), state=tk.DISABLED, bg="blue", fg="white")
saisie_joueur2.place(x=150, y=350)
saisie_joueur3 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 14), state=tk.DISABLED, bg="blue", fg="white")
saisie_joueur3.place(x=150, y=400)
saisie_joueur4 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 14), state=tk.DISABLED, bg="blue", fg="white")
saisie_joueur4.place(x=150, y=450)



def createfenetre():
    win = tk.Toplevel(root, bg="#55557f")

#root = tk.Tk() 
root.geometry("400x400") # mettre les pixels suivant ce pattern 0pixels x 0pixels
#root.configure(bg="cyan") # bg = background
root.minsize(800, 800)
root.maxsize(1000, 1000)
bouton = tk.Button(root, text='Entrez dans le jeu!!', font=("Helvetica", 14), height=3, width=15, bd=10, bg='orange', fg='Black', command=createfenetre)
# Afficher le bouton 
bouton.place(x=350, y=600)

#insertion image à l'interface graphique
from tkinter import PhotoImage
logo = PhotoImage(file="C:/Users/utilisateur/Google Drive/microsoft_ia/Trivial Pursuit/index.png")
logo_f = tk.Label(root, image = logo)
logo_f.place(x=5, y=600)


root.mainloop()



#insertion d'une image
#methode 1

#can=Canvas(root,width=500,height=500,background='white')
#canv.pack()

#rect=can.create_rectangle(10,10,100,200,fill="yellow")
#disque=can.create_oval(150,100,200,150,fill="red")
#oval=can.create_oval(150,200,200,350,fill="")
#ligne_1=can.create_line(150,80,450,250,fill="purple")
#ligne_2=can.create_line(450,20,200,150,width=3)
#poly=can.create_polygon(20,300,40,400,100,400,150,350)
#mon_image=PhotoImage(file="smiley.gif")
#img=can.create_image(250,250,image=mon_image)
#text_1=can.create_text(350,350,text="Hello World!",fill="red")
#text_2=can.create_text(300,400,text="Bonjour le monde!",font=("Helvetica",30))


#methode 2
#imageFile = "index.jpg"

#root.im1 = Image.open(imageFile)


#raw_input()
#window.mainloop()



