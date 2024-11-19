import json
import os

from models.base import Base

LOCATIONS = []


class Locations(Base):
    def __init__(self, root_path, is_debug=False):
        self.data_path = os.path.join(root_path, "data", "locations.json")
        self.load(is_debug)

    # This function returns the list of locations
    def get_locations(self):
        return self.data

    # This function returns the location with the given id
    # If the location with the given id does not exist, it returns None
    def get_location(self, location_id):
        for x in self.data:
            if x["id"] == location_id:
                return x
        return None
    
    # This function returns the locations in the warehouse with the given id
    # If the warehouse with the given id does not exist, it returns and empty list
    def get_locations_in_warehouse(self, warehouse_id):
        result = []
        for x in self.data:
            if x["warehouse_id"] == warehouse_id:
                result.append(x)
        return result

    # This function adds the given location to the list
    def add_location(self, location):
        location["created_at"] = self.get_timestamp()
        location["updated_at"] = self.get_timestamp()
        self.data.append(location)

    # This function updates the location with the given id, if the list contains a location with the given id
    def update_location(self, location_id, location):
        location["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == location_id:
                self.data[i] = location
                break

    # This function removes the location with the given id
    def remove_location(self, location_id):
        for x in self.data:
            if x["id"] == location_id:
                self.data.remove(x)

    # if debug is false this function loads the data from the locations.json file
    # if debug is true this function loads the data from the LOCATIONS list
    def load(self, is_debug):
        if is_debug:
            self.data = LOCATIONS
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    # This function saves the data of this object to the locations.json file
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
