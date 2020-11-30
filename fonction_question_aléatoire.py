def question_aleatoire(stock):
	data = Bdd()
	aleatoire_question = []
	stock_id_question = stock

    #choix aléatoire et affichage des deux thèmes,puis l'utilisateur doit faire un choix
	themes = data.lister_themes()
       themes_au_choix = random.sample(themes,2)
	print(themes_au_choix)
	theme_choisi = input(" ++++++  Veuillez choisir un theme: ")
   
    #stockage de tous les id, des libellés et des difficultés des questions du theme sélectionné par le joueur 
       
       liste_question = data.lister_questions_theme(theme_choisi)

    #choix aléatoire de la question
	
       aleatoire_question = random.sample(liste_question,1)
	while aleatoire_question[0][0] in stock_id_question : # [(5, 'ksjfle', 3), (6, 'isjape', 3)]
		aleatoire_question = random.sample(liste_question,1)

    #recupération des id des questions du theme choisis précédement par l'utilisateur
   
	id_question = aleatoire_question[0][0]
	stock_id_question.append(id_question)
       
    #rajout de toutes les questions supprimées si liste_question est vide 
	
       if len(liste_question) == 0:
              stock_id_question = []
      
    # récupération de la question aléatoire , des id_question, et du thème choisi
	
       return aleatoire_question[0], stock_id_question, theme_choisi
