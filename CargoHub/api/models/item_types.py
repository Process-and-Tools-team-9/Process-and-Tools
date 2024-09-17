import json

from models.base import Base

#Initializes an empty list to store the item types in.
ITEM_TYPES = []


class ItemTypes(Base):
    #initializes the itemtype and sets the path to item_types.json for data
    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "item_types.json"
        self.load(is_debug)

    #returns all the item types
    def get_item_types(self):
        return self.data
    
    #returns the itemtype based on id
    def get_item_type(self, item_type_id):
        for x in self.data:
            if x["id"] == item_type_id:
                return x
        return None

    #adds the itemtype to the json
    def add_item_type(self, item_type):
        item_type["created_at"] = self.get_timestamp()
        item_type["updated_at"] = self.get_timestamp()
        self.data.append(item_type)

    #updates the itemtype based on id
    def update_item_type(self, item_type_id, item_type):
        item_type["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == item_type_id:
                self.data[i] = item_type
                break

    #removes the itemtype from the json based on id
    def remove_item_type(self, item_type_id):
        for x in self.data:
            if x["id"] == item_type_id:
                self.data.remove(x)

    #reads the json
    def load(self, is_debug):
        if is_debug:
            self.data = ITEM_TYPES
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    #writes to the json
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
