from rich import print

class Headers:

    def menu_title(title):
        if title == "collaborater":
            print('[bold green]\n----------COLLABORATEURS----------[/bold green]')
        elif title == "customer":
            print('[bold green]\n----------CLIENTS----------[/bold green]')
        elif title == "contract":
            print('[bold green]\n----------CONTRATS----------[/bold green]')
        elif title == "event":
            print('[bold green]\n----------EVENNEMENTS----------[/bold green]')      


    def create_title(title) -> None:
        if title == "collaborater":
            print('[bold green]\n----------AJOUTER UN COLLABORATEUR----------[/bold green]')
        elif title == "customer":
            print('[bold green]\n----------AJOUTER UN CLIENT----------[/bold green]')
        elif title == "contract":
            print('[bold green]\n----------AJOUTER UN CONTRAT----------[/bold green]')
        elif title == "event":
            print('[bold green]\n----------AJOUTER UN EVENNEMENT----------[/bold green]')            


    def update_title(title) -> None:
        if title == "collaborater":
            print('[bold green]\n----------MODIFIER UN COLLABORATEUR----------[/bold green]')
        elif title == "customer":
            print('[bold green]\n----------MODIFIER UN CLIENT----------[/bold green]')
        elif title == "contract":
            print('[bold green]\n----------MODIFIER UN CONTRAT----------[/bold green]')
        elif title == "event":
            print('[bold green]\n----------MODIFIER UN EVENNEMENT----------[/bold green]')               

    def delete_title(title) -> None:
        if title == "collaborater":
            print('[bold green]\n----------SUPPRIMER UN COLLABORATEUR----------[/bold green]')
        elif title == "customer":
            print('[bold green]\n----------SUPPRIMER UN CLIENT----------[/bold green]')
        elif title == "contract":
            print('[bold green]\n----------SUPPRIMER UN CONTRAT----------[/bold green]')
        elif title == "event":
            print('[bold green]\n----------SUPPRIMER UN EVENNEMENT----------[/bold green]')                       