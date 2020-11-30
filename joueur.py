class Joueur:
    def __init__(self, *infos):
        self.nom = infos[0]
        self.tour = False
        self.camembert = ['1','2','3','4','5']    #liste des thèmes, on retire chaque chiffre correspondant à un thème validé

    def __str__(self):
        return self.nom

