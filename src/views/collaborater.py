from src.views.headers import Headers
import logging

class CollaboraterView:

    def menu_collaborater_view():
        """Menu collaborater"""
        title = "\n-----------------------Menu client---------------------------"
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

class CrudCollaboraterView:
    
    def create():
        Headers.create_title('customer')

        name = input(
        """
        Nom 
        --> """
    )
        
        role = input(
        """
        Ajouter à un groupe

        [1] - Gestion
        [2] - Commercial
        [3] - Support
        --> """
    )
        
        return  {'name' : name, 'role': role}  