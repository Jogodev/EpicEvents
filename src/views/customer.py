def menu_customer_view():
    """Menu player"""
    title = "\n-----------------------MENU CLIENT---------------------------"
    txt = """
            [1] - Ajouter un client
            [2] - Modifier un client
            [3] - Supprimer un client
            [4] - Liste de tous les clients
            [b] - retour au menu principal
            """
    print(title)
    print(txt)

    choice = input("Faites votre choix : ")
    return choice