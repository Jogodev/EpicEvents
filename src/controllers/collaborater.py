from src.views.collaborater import CollaboraterView, CrudCollaboraterView
import logging

class CollaboraterController:

    def menu_collaborater_controller(payload: dict):
        
        choice = CollaboraterView.menu_collaborater_view()
        if choice == "1":
            return "create_collaborater", payload
        elif choice == "b":
            return "main_menu", payload
        else:
            print("\nSaisie non valide\n")
            return "main_menu", payload
    
    
class CrudCollaboraterController:

    def create(payload):
        collaborater = CrudCollaboraterView.create() 
        logging.warning(collaborater)
        if collaborater['role'] == '1':
            collaborater['role'] = 'gestion'
        elif collaborater['role'] == '2':
            collaborater['role'] = 'commercial'
        elif collaborater['role'] == '3':    
            collaborater['role'] = 'support'

        logging.warning(collaborater)