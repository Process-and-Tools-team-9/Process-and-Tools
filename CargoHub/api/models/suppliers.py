import json
import os

from models.base import Base

SUPPLIERS = []


class Suppliers(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = os.path.join(root_path, "data", "suppliers.json")
        self.load(is_debug)

    # This function returns the list of suppliers
    def get_suppliers(self):
        return self.data

    # This function returns the supplier with the given id
    # If the supplier with the given id does not exist, it returns None
    def get_supplier(self, supplier_id):
        for x in self.data:
            if x["id"] == supplier_id:
                return x
        return None

    # This function adds the given supplier to the list
    # It also sets the created_at and updated_at fields of the time of the creation
    def add_supplier(self, supplier):
        supplier["created_at"] = self.get_timestamp()
        supplier["updated_at"] = self.get_timestamp()
        self.data.append(supplier)

    # This function updates the supplier with the given id, to the given supplier
    # if the list contains a supplier with the given id
    def update_supplier(self, supplier_id, supplier):
        supplier["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == supplier_id:
                self.data[i] = supplier
                break

    # This function removes the supplier with the given id
    # if the list contains a supplier with the given id
    def remove_supplier(self, supplier_id):
        for x in self.data:
            if x["id"] == supplier_id:
                self.data.remove(x)

    # if debug is false this function loads the data from the suppliers.json file
    # if debug is true this function loads the data from the SUPPLIERS list
    def load(self, is_debug):
        if is_debug:
            self.data = SUPPLIERS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    # This function saves the data of this object to the suppliers.json file
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
