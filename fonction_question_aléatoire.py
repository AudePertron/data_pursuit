def question_aleatoire(lister_themes,lister_questions_theme):
       
       liste_question = []
       question_aleatoire = []
       stock_id_question = []
       '''
       liste_question_finale = {}
       '''
       #choix aléatoire et affichage des deux thèmes,puis l'utilisateur doit faire un choix
       theme = sample(lister_themes,2)
       print(theme)
       theme = input("Veuillez choisir un theme: ")
       #stock des id des questions
       liste_question = id_question in lister_questions_theme(theme)
       #choix aléatoire d'un id_question 
       question_aleatoire = sample(liste_question,1) 
 '''   
        #creation d'un dictionnaire 
       for key, value in  liste_question:    
        liste_question_finale.setdefault(key,[]).append(value)
'''
       #recupération des id des questions déjà posées du theme choisis
       stock_id_question.append(id_question in question_aleatoire)
       #suppression des id_question dejà sélectionnées dans liste_question
       if id_question in (stock_id_question) and id_question in (liste_question):
           del liste_question[id_question]
       #rajout de toutes les questions supprimées si liste_question est vide 
       if len(liste_question) == 0:
          liste_question = liste_question + stock_id_question
