class CollaboraterView:

    def menu_collaborater_view():
        """Menu player"""
        title = "\n-----------------------MENU client---------------------------"
        txt = """
                        [1] - Ajouter un collaborateur
                        [2] - Modifier un collaborateur
                        [3] - Supprimer un collaborateur
                        [4] - Liste de tous les collaborateurs
                        [b] - retour au menu principal
                        """
        print(title)
        print(txt)

        choice = input("Faites votre choix : ")
        return choice
