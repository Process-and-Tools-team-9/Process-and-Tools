import json

from models.base import Base

#initializes an empty list to store item groups in
ITEM_GROUPS = []


class ItemGroups(Base):
    #initializes the item group and sets the path to the item_groups.json
    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "item_groups.json"
        self.load(is_debug)

    #returns all the item_groups data
    def get_item_groups(self):
        return self.data

    #returns all the item_group data ,based on the id that's passed in the params 
    def get_item_group(self, item_group_id):
        for x in self.data:
            if x["id"] == item_group_id:
                return x
        return None

    #adds a group_item to the data
    def add_item_group(self, item_group):
        item_group["created_at"] = self.get_timestamp()
        item_group["updated_at"] = self.get_timestamp()
        self.data.append(item_group)

    #updates a group_item based on the id that's passed 
    def update_item_group(self, item_group_id, item_group):
        item_group["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == item_group_id:
                self.data[i] = item_group
                break

    #removes the item_group based on id
    def remove_item_group(self, item_group_id):
        for x in self.data:
            if x["id"] == item_group_id:
                self.data.remove(x)

    #Reads the data for the program
    def load(self, is_debug):
        if is_debug:
            self.data = ITEM_GROUPS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    #Writes the data to the json
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
  