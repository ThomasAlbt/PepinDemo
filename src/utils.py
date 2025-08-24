import json, csv
from pathlib import Path
from .models import Client

# minimalist way to read a json

def load_json(path: str | Path):
    with open(path, encoding = 'utf-8') as f:
        return json.load(f)
    
# write in a json

def write_json(path: str | Path, client: Client):
    with open(path, 'r', encoding = 'utf-8') as f:
        data = json.load(f)

    data.append(client)

    with open(path, 'w', encoding = 'utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent = 4)


# write a csv based on the json we give it

def write_csv(path: str | Path, rows, fieldnames):
    path = Path(path) # we make sure path is a pathlib object with Path (we sure love pathing in  python i guess ahah)
    path.parent.mkdir(parents = True, exist_ok = True) # make sure the folder for the CSV exist, parents = true will create the folder if needed and exist_ok = true prevent and error if it already existed

    with path.open("w") as f: #opening CSV in write mode
        w = csv.DictWriter(f, fieldnames = fieldnames) # DictWriter is an object to make us write in the csv, with our fieldnames as headers
        w.writeheader # write the header we define above
        w.writerows(rows) # write the rows we gave it