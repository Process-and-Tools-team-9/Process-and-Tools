import json
import os

from models.base import Base
from providers import data_provider

ORDERS = []


class Orders(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = os.path.join(root_path, "data", "orders.json")
        self.load(is_debug)

    # This function returns the list of orders
    def get_orders(self):
        return self.data

    # This function returns the order with the given id
    # If the order with the given id does not exist, it returns None
    def get_order(self, order_id):
        for x in self.data:
            if x["id"] == order_id:
                return x
        return None

    # This function returns the items in the order with the given id
    # If the order with the given id does not exist, it returns None
    def get_items_in_order(self, order_id):
        for x in self.data:
            if x["id"] == order_id:
                return x["items"]
        return None

    # This function returns the orders in the shipment with the given id
    # If the shipment with the given id does not exist, it returns an empty list
    def get_orders_in_shipment(self, shipment_id):
        result = []
        for x in self.data:
            if x["shipment_id"] == shipment_id:
                result.append(x["id"])
        return result

    # This function returns the orders for the client with the given id
    # If the client with the given id does not exist, it returns an empty list
    def get_orders_for_client(self, client_id):
        result = []
        for x in self.data:
            if x["ship_to"] == client_id or x["bill_to"] == client_id:
                result.append(x)
        return result

    # This function adds the given order to the list
    # It also sets the created_at and updated_at fields of the time of the creation
    def add_order(self, order):
        order["created_at"] = self.get_timestamp()
        order["updated_at"] = self.get_timestamp()
        self.data.append(order)

    # This function updates the order with the given id, if the list contains a order with the given id
    # This function also updates the updated_at field of the time to the time of update
    def update_order(self, order_id, order):
        order["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == order_id:
                self.data[i] = order
                break

    # This function updates the items in the order with the given id
    def update_items_in_order(self, order_id, items):
        order = self.get_order(order_id)
        current = order["items"]
        for x in current:
            found = False
            for y in items:
                if x["item_id"] == y["item_id"]:
                    found = True
                    break
            if not found:
                inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                min_ordered = 1_000_000_000_000_000_000
                min_inventory
                for z in inventories:
                    if z["total_allocated"] > min_ordered:
                        min_ordered = z["total_allocated"]
                        min_inventory = z
                min_inventory["total_allocated"] -= x["amount"]
                min_inventory["total_expected"] = z["total_on_hand"] + z["total_ordered"]
                data_provider.fetch_inventory_pool().update_inventory(min_inventory["id"], min_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                    min_ordered = 1_000_000_000_000_000_000
                    for z in inventories:
                        if z["total_allocated"] < min_ordered:
                            min_ordered = z["total_allocated"]
                            min_inventory = z
                min_inventory["total_allocated"] += y["amount"] - x["amount"]
                min_inventory["total_expected"] = z["total_on_hand"] + z["total_ordered"]
                data_provider.fetch_inventory_pool().update_inventory(min_inventory["id"], min_inventory)
        order["items"] = items
        self.update_order(order_id, order)

    # This function updates the orders in the shipment with the given id
    # It removes the orders that are not in the given list
    def update_orders_in_shipment(self, shipment_id, orders):
        packed_orders = self.get_orders_in_shipment(shipment_id)
        for x in packed_orders:
            if x not in orders:
                order = self.get_order(x)
                order["shipment_id"] = -1
                order["order_status"] = "Scheduled"
                self.update_order(x, order)
        for x in orders:
            order = self.get_order(x)
            order["shipment_id"] = shipment_id
            order["order_status"] = "Packed"
            self.update_order(x, order)

    # This function removes the order with the given id
    # if the list contains a order with the given id
    def remove_order(self, order_id):
        for x in self.data:
            if x["id"] == order_id:
                self.data.remove(x)

    # if debug is false this function loads the data from the orders.json file
    # if debug is true this function loads the data from the ORDERS list
    def load(self, is_debug):
        if is_debug:
            self.data = ORDERS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    # This function saves the data of this object to the orders.json file
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
