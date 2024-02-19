def menu_event_view():
    """Menu evenT"""
    title = "\n-----------------------MENU EVENNEMENTS---------------------------"
    txt = """
            [1] - Ajouter un evennement
            [2] - Modifier un evennement
            [3] - Supprimer un evennement
            [4] - Liste de tous les evennements
            [b] - retour au menu principal
            """
    print(title)
    print(txt)

    choice = input("Faites votre choix : ")
    return choice
