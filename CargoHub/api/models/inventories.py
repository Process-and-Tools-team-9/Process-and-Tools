import json

from models.base import Base

#Initializes an empty list to store the inventories in.
INVENTORIES = []

#The Client class with the structure
class Inventories(Base):
     #Initializes the inventories and sets the path to the inventories.json for data
    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "inventories.json"
        self.load(is_debug)

    #Returns all the inventories data
    def get_inventories(self):
        return self.data

    #Returns inventory data, based on id
    def get_inventory(self, inventory_id):
        for x in self.data:
            if x["id"] == inventory_id:
                return x
        return None

    #Returns all the inventories ,based on an item_id
    def get_inventories_for_item(self, item_id):
        result = []
        for x in self.data:
            if x["item_id"] == item_id:
                result.append(x)
        return result

    #Returns the result of what excpected, ordered, allocated, 
    #available of the item that's passed in the parameters 
    def get_inventory_totals_for_item(self, item_id):
        result = {
            "total_expected": 0,
            "total_ordered": 0,
            "total_allocated": 0,
            "total_available": 0
        }
        for x in self.data:
            if x["item_id"] == item_id:
                result["total_expected"] += x["total_expected"]
                result["total_ordered"] += x["total_ordered"]
                result["total_allocated"] += x["total_allocated"]
                result["total_available"] += x["total_available"]
        return result

    #Adds a new item to inventory,json
    def add_inventory(self, inventory):
        inventory["created_at"] = self.get_timestamp()
        inventory["updated_at"] = self.get_timestamp()
        self.data.append(inventory)

    #Updates an existing item based on inventory_id in invenotries.json
    def update_inventory(self, inventory_id, inventory):
        inventory["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == inventory_id:
                self.data[i] = inventory
                break

    #Removes an inventory
    def remove_inventory(self, inventory_id):
        for x in self.data:
            if x["id"] == inventory_id:
                self.data.remove(x)

    #Reads the data from the json file in order for the program to use it
    def load(self, is_debug):
        if is_debug:
            self.data = INVENTORIES
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    #Writes the data to the json file
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
