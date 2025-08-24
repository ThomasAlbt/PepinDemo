import json, csv
from pathlib import Path

# minimalist way to read a json

def load_json(path):
    with open(path) as f:
        return json.load(f)
    
# write a csv based on the json we give it

def write_csv(path, rows, fieldnames):
    path = Path(path) # we make sure path is a pathlib object with Path (we sure love pathing in  python i guess ahah)
    path.parent.mkdir(parents = True, exist_ok = True) # make sure the folder for the CSV exist, parents = true will create the folder if needed and exist_ok = true prevent and error if it already existed

    with path.open("w") as f: #opening CSV in write mode
        w = csv.DictWriter(f, fieldnames = fieldnames) # DictWriter is an object to make us write in the csv, with our fieldnames as headers
        w.writeheader # write the header we define above
        w.writerows(rows) # write the rows we gave it