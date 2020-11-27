import tkinter as tk
from tkinter import PhotoImage

colors = {
    'orange':'#f9690c',
    'noir':'#030100',
    'blanc' :'#f9f5f5'
}

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Pursuit")
        self.master.geometry('1200x600')
        self.master.minsize(900, 600)
        self.master.configure(bg=colors['noir'])

        # titre
        titre = tk.Label(self.master, text='Bienvenue sur le jeu Data Pursuit', 
                        font=("Helvetica", 20), bg=colors['orange'] , fg=colors['noir'])
        titre.pack(fill='x', side='top')

        #frame boutons
        self.frame_boutons = tk.Frame(self.master, bg=colors['blanc'])
        self.frame_boutons.pack(pady=25)

        #frame menu
        self.frame_menu = tk.Frame(self.master, bg=colors['noir'])
        self.frame_menu.pack()

        #fonction d'ajout de bouton
        p_joueur = tk.Entry(self.frame_boutons, width=30).grid(row=1, column=1)

        def nb_j():
            nb_joueurs = p_joueur.get()
            return nb_joueurs

        tk.Button(master, text='Valider', command = nb_joueurs).grid(row=1, column=2)

def main():
    window = tk.Tk()
    Interface(window)
    window.mainloop()

main()
        # for i, (key, value) in enumerate(fonctions.items()):
        #     ligne = tk.Button(self.frame_boutons, height=2, width=12, bg=colors['orange'], bd=0, font=(
        #         'Helvetica', '12'), text=key, command=value)
        #     ligne.grid(row=0, column=i, padx=5, ipadx=12)



    # def afficher_joueur(self):
    #     for widget in self.frame_menu.winfo_children():
    #         widget.pack_forget()

    #     credit_frame = tk.Frame(self.frame_menu, bg=color['blanc'])
    #     credit_frame.pack()

    #     credit= fonctions   ###importer fonction affichage?

    #     credit_label = tk.Label(credit_frame, text="credit", bg=colors['blanc'], font=(
    #         'Helvetica', '20', 'underline'))
    #     credit_label.grid(row=0, column=1, padx=50)

    #     for i, value in enumerate(credit, 1):
    #         label = tk.Label(credit_frame, text=value,
    #                         bg=colors['blanc'], font=('Helvetica', '12'))
    #         label.grid(row=i, column=1)