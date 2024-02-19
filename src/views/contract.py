def menu_contract_view():
    """Menu contract"""
    title = "\n-----------------------MENU CONTRATS---------------------------"
    txt = """
            [1] - Ajouter un contrat
            [2] - Modifier un contrat
            [3] - Supprimer un contrat
            [4] - Liste de tous les contrats
            [b] - retour au menu principal
            """
    print(title)
    print(txt)

    choice = input("Faites votre choix : ")
    return choice