from models.warehouses import Warehouses
from models.locations import Locations
from models.transfers import Transfers
from models.items import Items
from models.item_lines import ItemLines
from models.item_groups import ItemGroups
from models.item_types import ItemTypes
from models.inventories import Inventories
from models.suppliers import Suppliers
from models.orders import Orders
from models.clients import Clients
from models.shipments import Shipments
import os


# DEBUG is either True or False
# If True then the program runs in debug mode and gives additional information
# If False then the program doesn't run in debug mode and does not give the additional information whilst running.
DEBUG = False

#The root path of all the data that's contained in this project


ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))



_warehouses = None
_locations = None
_transfers = None
_items = None
_item_lines = None
_item_groups = None
_item_types = None
_inventories = None
_suppliers = None
_orders = None
_shipments = None
_clients = None

#This is where the objects are initialized with the root path and the debug settings
def init():
    global _warehouses
    _warehouses = Warehouses(ROOT_PATH, DEBUG)
    global _locations
    _locations = Locations(ROOT_PATH, DEBUG)
    global _transfers
    _transfers = Transfers(ROOT_PATH, DEBUG)
    global _items
    _items = Items(ROOT_PATH, DEBUG)
    global _item_lines
    _item_lines = ItemLines(ROOT_PATH, DEBUG)
    global _item_groups
    _item_groups = ItemGroups(ROOT_PATH, DEBUG)
    global _item_types
    _item_types = ItemTypes(ROOT_PATH, DEBUG)
    global _inventories
    _inventories = Inventories(ROOT_PATH, DEBUG)
    global _suppliers
    _suppliers = Suppliers(ROOT_PATH, DEBUG)
    global _orders
    _orders = Orders(ROOT_PATH, DEBUG)
    global _clients
    _clients = Clients(ROOT_PATH, DEBUG)
    global _shipments
    _shipments = Shipments(ROOT_PATH, DEBUG)


#These functions below return the objects, so that the objects could be used in other files of the program.
def fetch_warehouse_pool():
    return _warehouses


def fetch_location_pool():
    return _locations


def fetch_transfer_pool():
    return _transfers


def fetch_item_pool():
    return _items


def fetch_item_line_pool():
    return _item_lines


def fetch_item_group_pool():
    return _item_groups


def fetch_item_type_pool():
    return _item_types


def fetch_inventory_pool():
    return _inventories


def fetch_supplier_pool():
    return _suppliers


def fetch_order_pool():
    return _orders


def fetch_client_pool():
    return _clients


def fetch_shipment_pool():
    return _shipments
