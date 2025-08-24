from src.service import (
    load_clients,
    filter_by_country,
    export_csv,
    generate_email_openai
)

def main():
    clients = load_clients("list_client.json")
    fr = filter_by_country(clients, "France")

    export = export_csv(fr, "export/clients_fr.csv")
    print(f"{len(fr)} clients exportés -> {export}")

    if fr:
        print("Exemple d'email généré par OpenAI:")
        print(generate_email_openai(fr[0]))

if __name__ == "__main__":
    main()