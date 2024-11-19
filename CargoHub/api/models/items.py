import json
import os

from models.base import Base

#Initializes an empty list to store the clients in.
ITEMS = []


#The Items class with the structure
class Items(Base): 
    #Initializes the item and sets the path to the item.json for data
    def __init__(self, root_path, is_debug=False):
        self.data_path = os.path.join(root_path, "data", "items.json")
        self.load(is_debug)

    #returns all the items
    def get_items(self):
        return self.data

    #returns the item based on id.
    def get_item(self, item_id):
        for x in self.data:
            if x["id"] == item_id:
                return x
        return None

    #returns all the items based on item_line_id.
    def get_items_for_item_line(self, item_line_id):
        result = []
        for x in self.data:
            if x["item_line_id"] == item_line_id:
                result.append(x["id"])
        return result

    #returns all the items based on item_group_id
    def get_items_for_item_group(self, item_group_id):
        result = []
        for x in self.data:
            if x["item_group_id"] == item_group_id:
                result.append(x["id"])
        return result
    
    #returns all the items based on item_type_id
    def get_items_for_item_type(self, item_type_id):
        result = []
        for x in self.data:
            if x["item_type_id"] == item_type_id:
                result.append(x["id"])
        return result

    #returns all the items based on the supplier_id
    def get_items_for_supplier(self, supplier_id):
        result = []
        for x in self.data:
            if x["supplier_id"] == supplier_id:
                result.append(x)
        return result

    #adds item to the json
    def add_item(self, item):
        item["created_at"] = self.get_timestamp()
        item["updated_at"] = self.get_timestamp()
        self.data.append(item)

    #udpates item from the json based on item_id
    def update_item(self, item_id, item):
        item["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == item_id:
                self.data[i] = item
                break

    #removes item from the json based on item_id
    def remove_item(self, item_id):
        for x in self.data:
            if x["id"] == item_id:
                self.data.remove(x)

    #reads the json
    def load(self, is_debug):
        if is_debug:
            self.data = ITEMS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    #writes to the json
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
