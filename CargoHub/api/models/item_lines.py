import json

from models.base import Base

#initializes an empty list to store the item_lines
ITEM_LINES = []

#The ItemLines class with the structure
class ItemLines(Base):
    #Initializes the itemLines and sets the path to the item_lines.json for the data
    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "item_lines.json"
        self.load(is_debug)

    #returns all the item lines
    def get_item_lines(self):
        return self.data

    #gets the item based on id. from the json
    def get_item_line(self, item_line_id):
        for x in self.data:
            if x["id"] == item_line_id:
                return x
        return None

    #adds the item to the json
    def add_item_line(self, item_line):
        item_line["created_at"] = self.get_timestamp()
        item_line["updated_at"] = self.get_timestamp()
        self.data.append(item_line)

    #updates the itemline based on id.
    def update_item_line(self, item_line_id, item_line):
        item_line["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == item_line_id:
                self.data[i] = item_line
                break

    #deletes the itemline based on id
    def remove_item_line(self, item_line_id):
        for x in self.data:
            if x["id"] == item_line_id:
                self.data.remove(x)

    #reads the json
    def load(self, is_debug):
        if is_debug:
            self.datathe = ITEM_LINES
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    #writes to the json
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
