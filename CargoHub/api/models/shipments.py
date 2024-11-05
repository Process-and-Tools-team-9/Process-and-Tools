import json

from models.base import Base
from providers import data_provider

SHIPMENTS = []


class Shipments(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "shipments.json"
        self.load(is_debug)

    # This function returns the list of shipments
    def get_shipments(self):
        return self.data

    # This function returns the shipment with the given id
    # If the shipment with the given id does not exist, it returns None
    def get_shipment(self, shipment_id):
        for x in self.data:
            if x["id"] == shipment_id:
                return x
        return None

    # This function returns the items in the shipment with the given id
    # If the shipment with the given id does not exist, it returns None
    def get_items_in_shipment(self, shipment_id):
        for x in self.data:
            if x["id"] == shipment_id:
                return x["items"]
        return None

    # This function adds the given shipment to the list
    # It also sets the created_at and updated_at fields of the time of the creation
    def add_shipment(self, shipment):
        shipment["created_at"] = self.get_timestamp()
        shipment["updated_at"] = self.get_timestamp()
        self.data.append(shipment)

    # This function updates the shipment with the given id, if the list contains a shipment with the given id
    def update_shipment(self, shipment_id, shipment):
        shipment["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == shipment_id:
                self.data[i] = shipment
                break

    
    def update_items_in_shipment(self, shipment_id, items):
        shipment = self.get_shipment(shipment_id)
        current = shipment["items"]
        for x in current:
            found = False
            for y in items:
                if x["item_id"] == y["item_id"]:
                    found = True
                    break
            if not found:
                inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                max_ordered = -1
                max_inventory
                for z in inventories:
                    if z["total_ordered"] > max_ordered:
                        max_ordered = z["total_ordered"]
                        max_inventory = z
                max_inventory["total_ordered"] -= x["amount"]
                max_inventory["total_expected"] = z["total_on_hand"] + z["total_ordered"]
                data_provider.fetch_inventory_pool().update_inventory(max_inventory["id"], max_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                    max_ordered = -1
                    for z in inventories:
                        if z["total_ordered"] > max_ordered:
                            max_ordered = z["total_ordered"]
                            max_inventory = z
                    max_inventory["total_ordered"] += y["amount"] - x["amount"]
                    max_inventory["total_expected"] = z["total_on_hand"] + z["total_ordered"]
                    data_provider.fetch_inventory_pool().update_inventory(max_inventory["id"], max_inventory)
        shipment["items"] = items
        self.update_shipment(shipment_id, shipment)

    # This function removes the shipment with the given id
    # if the list contains a shipment with the given id
    def remove_shipment(self, shipment_id):
        for x in self.data:
            if x["id"] == shipment_id:
                self.data.remove(x)

    # if debug is false this function loads the data from the shipments.json file
    # if debug is true this function loads the data from the SHIPMENTS list
    def load(self, is_debug):
        if is_debug:
            self.data = SHIPMENTS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    # This function saves the data of this object to the shipments.json file
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
