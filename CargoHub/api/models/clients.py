import json
import os

from models.base import Base

#Initializes an empty list to store the clients in.
CLIENTS = []

#The Client class with the structure
class Clients(Base):
    #Initializes the client and sets the path to the clients.json for data
    def __init__(self, root_path, is_debug=False):
        self.data_path = os.path.join(root_path, "data", "clients.json")
        self.load(is_debug)

    #Returns all the clients data
    def get_clients(self):
        return self.data

    #Returns the client data, based on id
    def get_client(self, client_id):
        for x in self.data:
            if x["id"] == client_id:
                return x
        return None

    #Adds a new client to json with the parameters passed as data
    def add_client(self, client):
        client["created_at"] = self.get_timestamp()
        client["updated_at"] = self.get_timestamp()
        self.data.append(client)

    #Updates an existing client based on the ID passed in the parameters
    def update_client(self, client_id, client):
        client["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == client_id:
                self.data[i] = client
                break

    #Removes a client from  clients.json based on the id 
    def remove_client(self, client_id):
        for x in self.data:
            if x["id"] == client_id:
                self.data.remove(x)

    #Reads in the data from clients.json in order for the program to use is
    def load(self, is_debug):
        if is_debug:
            self.data = CLIENTS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    #Writes the data to the clients.json.
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
