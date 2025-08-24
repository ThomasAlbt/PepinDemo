class Client: 
    def __init__(self, id, name, email, country, notes):
        self.id = id
        self.name = name
        self.email = email
        self.country = country
        self.notes = notes

    def get_infos(self) -> str:
        return f"{self.name} ({self.email} - {self.country})"
    
# Forces types to all the variables with the constructor, get_infos is forced to return a string as well