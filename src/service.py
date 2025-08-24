from pathlib import Path
from typing import List
from openai import OpenAI
from .models import Client
from .utils import load_json, write_csv

import os
from dotenv import load_dotenv

load_dotenv()

def load_clients(path) -> List[Client]: # make sure we reutnr an array with objects that respect Client variables
    data = load_json(path)
    return [Client(**item) for item in data] # create an array of object with data

def filter_by_country(clients, country) -> List[Client]:
    return [client for client in clients if client.country.lower() == country.lower()] # that syntax is something but at least its compact

def export_csv(clients, path) -> Path:
    rows = [client.__dict__ for client in clients] # create the rows needed to write our csv
    write_csv(path, rows, fieldnames=["id", "name", "email", "country", "notes"]) # use the write csv function we did
    return Path(path) # return the path of the csv we just created

def generate_email_openai(client):

    # ai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # prompt = f"""
    # écris un email professionel et amical a un client.
    # Nom du client: {client.name}
    # Notes sur le client: {client.notes}
    # Propose leurs de nous rappeler avec notre numéro 06 12 34 56 78
    # signe en tant que l'entreprise Pépin
    # """

    # result = ai_client.chat.completions.create(
    #     model = "gpt-5-mini",
    #     messages = [{"role": "user", "content": prompt}],
    #     temperature = 0.6
    # )

    # Code above work with openai api, however it doesnt have free access anymore so i mocked the AI response

    return f"Bonjour {client.name},\nNotes du client: {client.notes}\nMerci pour votre message. Appelez-nous au 06 12 34 56 78.\nCordialement, Pépin"