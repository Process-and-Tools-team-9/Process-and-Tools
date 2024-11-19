import json
import os

from models.base import Base

WAREHOUSES = []


class Warehouses(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = os.path.join(root_path, "data", "warehouses.json")
        self.load(is_debug)

    # This function returns the list of warehouses
    def get_warehouses(self):
        return self.data

    # This function returns the warehouse with the given id
    # If the warehouse with the given id does not exist, it returns None
    def get_warehouse(self, warehouse_id):
        for x in self.data:
            if x["id"] == warehouse_id:
                return x
        return None

    # This function adds a warehouse to the list
    # It also sets the created_at and updated_at fields of the time of the creation
    def add_warehouse(self, warehouse):
        warehouse["created_at"] = self.get_timestamp()
        warehouse["updated_at"] = self.get_timestamp()
        self.data.append(warehouse)


    # This function updates the warehouse with the given id, if the list contains a warehouse with the given id
    # It also sets the updated_at field of the time of the updates
    def update_warehouse(self, warehouse_id, warehouse):
        warehouse["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == warehouse_id:
                self.data[i] = warehouse
                break

    # This function removes the warehouse with the given id if the list contains a warehouse with the given id
    def remove_warehouse(self, warehouse_id):
        for x in self.data:
            if x["id"] == warehouse_id:
                self.data.remove(x)

    # if debug is false this function loads the data from the warehouses.json file
    # if debug is true this function loads the data from the WAREHOUSES list
    def load(self, is_debug):
        if is_debug:
            self.data = WAREHOUSES
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    # this updates the json with the current WAREHOUSES list
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
