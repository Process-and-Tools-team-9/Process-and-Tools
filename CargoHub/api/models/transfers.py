import json
import os
from models.base import Base

TRANSFERS = []


class Transfers(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = os.path.join(root_path, "data", "transfers.json")
        self.load(is_debug)

    # This function returns the list of transfers
    def get_transfers(self):
        return self.data

    # This function returns the transfer with the given id
    # If the transfer with the given id does not exist, it returns None
    def get_transfer(self, transfer_id):
        for x in self.data:
            if x["id"] == transfer_id:
                return x
        return None

    # This function returns the items in the transfer with the given id
    # If the transfer with the given id does not exist, it returns None
    def get_items_in_transfer(self, transfer_id):
        for x in self.data:
            if x["id"] == transfer_id:
                return x["items"]
        return None

    # This function adds the given transfer to the list
    # It also sets the created_at and updated_at fields of the time of the creation, and sets the status to scheduled
    def add_transfer(self, transfer):
        transfer["transfer_status"] = "Scheduled"
        transfer["created_at"] = self.get_timestamp()
        transfer["updated_at"] = self.get_timestamp()
        self.data.append(transfer)

    # This function updates the transfer with the given id, if the list contains a transfer with the given id
    # This function also updates the updated_at field of the time to the time of update
    def update_transfer(self, transfer_id, transfer):
        transfer["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == transfer_id:
                self.data[i] = transfer
                break

    
    def remove_transfer(self, transfer_id):
        for x in self.data:
            if x["id"] == transfer_id:
                self.data.remove(x)

    # if debug is false this function loads the data from the transfers.json file
    # if debug is true this function loads the data from the TRANSFERS list
    def load(self, is_debug):
        if is_debug:
            self.data = TRANSFERS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    # this updates the json with the current TRANSFERS list
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
