from src.views.collaborater import CollaboraterView

class CollaboraterController():

    def menu_collaborater_controller(payload: dict):
        
        choice = CollaboraterView.menu_collaborater_view()
        if choice == "1":
            return "create_collaborater", payload
        elif choice == "b":
            return "main_menu", payload
        else:
            print("\nSaisie non valide\n")
            return "main_menu", payload
    
    
