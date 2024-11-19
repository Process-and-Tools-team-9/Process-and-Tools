import requests

# python -m pytest items_it.py

# TODO: replace with test server url
BASE_URL = "http://localhost:3000/api/v1"
header = {"api_key": "a1b2c3d4e5"}


item = {
        "uid": "P000001",
        "code": "sjQ23408K",
        "description": "Face-to-face clear-thinking complexity",
        "short_description": "must",
        "upc_code": "6523540947122",
        "model_number": "63-OFFTq0T",
        "commodity_code": "oTo304",
        "item_line": 11,
        "item_group": 73,
        "item_type": 14,
        "unit_purchase_quantity": 47,
        "unit_order_quantity": 13,
        "pack_order_quantity": 11,
        "supplier_id": 34,
        "supplier_code": "SUP423",
        "supplier_part_number": "E-86805-uTM",
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
    }

#### TESTS ####

#The ones that do not work dont work because they are trying to take an id but an item does not have an id
#Item type lines en groups do have id's
#To fix this we can take a look at the uid

def test_get_all_items():
    response = requests.get(f"{BASE_URL}/items",headers=header)
    assert response.status_code == 200

#DOES NOT WORK
#CODE SHOULD BE FIXED
def test_get_item_by_id():
    response = requests.get(f"{BASE_URL}/items/1",headers=header)
    assert response.status_code == 200


def test_create_item():
    response = requests.post(f"{BASE_URL}/items", json=item, headers=header)
    assert response.status_code == 201

#DOES NOT WORK
#CODE SHOULD BE FIXED
def test_update_item():
    response = requests.put(f"{BASE_URL}/items/1", json=item, headers=header)
    assert response.status_code == 200


#DOES NOT WORK
#CODE SHOULD BE FIXED
def test_delete_item():
    response = requests.delete(f"{BASE_URL}/items/1", headers=header)
    assert response.status_code == 200

def get_items_for_supplier():
    response = requests.get(f"{BASE_URL}/supplier/34/items", headers=header)
    assert response.status_code == 200

def get_items_for_item_line():
    response = requests.get(f"{BASE_URL}/item_line/11/items", headers=header)
    assert response.status_code == 200

def get_items_for_item_group():
    response = requests.get(f"{BASE_URL}/item_group/73/items", headers=header)
    assert response.status_code == 200

def get_items_for_item_type():
    response = requests.get(f"{BASE_URL}/item_type/14/items", headers=header)
    assert response.status_code == 200




