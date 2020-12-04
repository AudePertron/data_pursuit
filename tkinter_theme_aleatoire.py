# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:05:30 2020

@author: utilisateur
"""
from connect_bdd import Bdd
import random
from tkinter import*
from random import sample

stock = []
theme = []
difficulte = []
from connect_bdd import Bdd


def tkinter_theme_aleatoire():
    #a = str(input("nom du theme?:"))
    #création du dicitonnaire de coleur 
    dico = {1:"blue",2:"red",3:"purple",4:"orange",5:"green"}
    #récupération de tous les theme de la base de donnée via la fonction lister_theme
    themes = Bdd.lister_themes()
    #choix aléatoire du theme
    themes_au_choix = random.sample(themes,2)
    #récupération des id des themes présent dans la liste aléatoire
    id_theme = themes_au_choix[0][0],themes_au_choix[1][0]
    #récupération des libellé des themes présent dans la liste aléatoire
    libelle_theme = themes_au_choix[0][1],themes_au_choix[1][1]
    print(libelle_theme)
    #affichage des themes choisis aléatoirement, de leur id et de leur libellé
    #print(themes_au_choix,id_theme,libelle_theme)
 
   
   #création de la fenêtre
    
    fenetre_principale = Tk()
    
    #personnalisation''
    #titre
    fenetre_principale.title("Thème")
    
    #largeur de la fenêtre
    fenetre_principale.geometry("480x360")
    
    #largeur minimale
    fenetre_principale.minsize(360,360)
    
    #changement du logo de fenetre_principale
    fenetre_principale.iconbitmap("index.ico")
    
    #changement de la couleur de fond
    fenetre_principale.config(background="#55557f")
    
    #Titre
    fenetre_principale_titre = Label(fenetre_principale,text="Choisissez un theme", font=("Bradley Hand ITC",30),bg= "#55557f",fg="white")
    
    #le ccopyrigth en bas de la fenêtre
    fenetre_principale_copyrigth = Label(fenetre_principale,text="Tival pursuit by Aude,Celine,Ludivine & Luigi", font=("Bradley Hand ITC",8),bg= "#55557f",fg="white")
    
    #création de la frame bouton pour les boutons
    frame = Frame (fenetre_principale,bg="#55557f",bd=0,relief=SUNKEN)
   
    #création des boutons
    j = 0
    for i in id_theme:
        color = dico[i]
        if j == 0:
            theme1_bouton =Button (frame,text = libelle_theme[0],font=("Algerian",11),bg= color,fg="white",height = 10, width = 20, command=lambda: OnButtonClick(1))
        if j ==1:
            theme2_bouton =Button (frame,text = libelle_theme[1],font=("Algerian",11),bg= color,fg="white",height = 10, width = 20, command=lambda: OnButtonClick(2))
        j +=1
        print (color)
    
    def OnButtonClick(bouton):
       
       global choix,nom_theme
       if bouton ==1:
          nom_theme = libelle_theme[0]
          choix = id_theme[0]
       if bouton ==2: 
          nom_theme = libelle_theme[1]
          choix = id_theme[1]
   
    #mise en place des boutons côte à côte
    theme1_bouton.grid(row=0,column=0)
    theme2_bouton.grid(row=0,column=1,padx=10)
    #affichage du titre principal                           
    fenetre_principale_titre.pack()
    #expansion de la frame
    frame.pack(expand=TRUE)

    
    #affichage du copyrigth  
    fenetre_principale_copyrigth.pack(side=BOTTOM)
    #affichage de la fenêtre
    fenetre_principale.mainloop()
    #print("affichage",choix)
    return choix,nom_theme#, id_theme
print(tkinter_theme_aleatoire())