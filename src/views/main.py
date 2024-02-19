def main_menu_view():
    """Main menu"""

    title = "----------MENU----------"
    txt = """
         [1] - Collaborateur
         [2] - Clients
         [3] - Contrats
         [4] - Evennements
        """
    print(title)
    print(txt)
    choice = input("Faites votre choix : ")
    return choice