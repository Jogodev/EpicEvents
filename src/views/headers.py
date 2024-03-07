from rich import print

class Headers:
    def create_title(title) -> None:
        if title == "collaborater":
            print('[bold green]\n----------AJOUTER UN COLLABORATER----------[/bold green]')
        elif title == "customer":
            print('[bold green]\n----------AJOUTER UN CLIENT----------[/bold green]')
        elif title == "contract":
            print('[bold green]\n----------AJOUTER UN CONTRAT----------[/bold green]')
        elif title == "event":
            print('[bold green]\n----------AJOUTER UN EVENNEMENT----------[/bold green]')            


    def update_title(title) -> None:
        if title == "collaborater":
            print('[bold green]\n----------MODIFIER UN COLLABORATER----------[/bold green]')
        elif title == "customer":
            print('[bold green]\n----------MODIFIER UN CLIENT----------[/bold green]')
        elif title == "contract":
            print('[bold green]\n----------MODIFIER UN CONTRAT----------[/bold green]')
        elif title == "event":
            print('[bold green]\n----------MODIFIER UN EVENNEMENT----------[/bold green]')               

    def delete_title(title) -> None:
        if title == "collaborater":
            print('[bold green]\n----------SUPPRIMER UN COLLABORATER----------[/bold green]')
        elif title == "customer":
            print('[bold green]\n----------SUPPRIMER UN CLIENT----------[/bold green]')
        elif title == "contract":
            print('[bold green]\n----------SUPPRIMER UN CONTRAT----------[/bold green]')
        elif title == "event":
            print('[bold green]\n----------SUPPRIMER UN EVENNEMENT----------[/bold green]')                       