from src.service import (
    load_clients,
    filter_by_country,
    export_csv,
    generate_email_openai,
    add_client,
    delete_client
)

def main():

    clients = load_clients("list_client.json")

    action = input("Choose your action: [READ/add/remove/email]") or "read"

    match action:
        case "Add" | "add":
            client = {
                "id": load_clients("list_client.json")[-1].id + 1,
                "name": input("Nom du client:"),
                "email": input("Email du client:"),
                "country": input("Pays du client:"),
                "notes": input("Notes sur le client:")
            }
            add_client("list_client.json", client)
            print("Yippeee")
        case "Remove" | "REMOVE" | "remove":
            for client in clients:
                print(f"[{client.id}] {client.name} ({client.email}) - {client.country}")
            client_id = int(input("Quel id client voulez vous supprimer ?"))
            if client_id:
                validation = input("Etes vous sur ? [y/N]") or "N"
                if validation in ("N", "n"):
                    return
                elif validation in ("Y", "y"):
                    delete_client("list_client.json", client_id)
                    print(f"RIP {client_id}")
            else:
                print("Client n'existe pas")
        case "Read" | "read":
            filtering = input("Voulez vous trier par pays ? [y/N]") or "N"
            match filtering:
                case "y" | "Y":
                    country = input("Entrer le pays:") or "France"
                    country_filtered = filter_by_country(clients, country)
                    export = export_csv(country_filtered, f"export/clients_{country}.csv")
                    print(f"{len(country_filtered)} clients exportés -> {export}")
                case "n" | "N":
                    export = export_csv(clients, "export/clients_all.csv")
                    print(f"Tout les clients exportés -> {export}")
        case "Email" | "email":
            for client in clients:
                print(f"[{client.id}] {client.name} ({client.email}) - {client.country}")
            client_id = int(input("A quel id client faut il envoyer le mail ?"))
            if client_id:
                print("Exemple d'email généré par OpenAI:")
                print(generate_email_openai(clients[client_id - 1]))
            else:
                "Ceci n'est pas un nombre."

if __name__ == "__main__":
    main()