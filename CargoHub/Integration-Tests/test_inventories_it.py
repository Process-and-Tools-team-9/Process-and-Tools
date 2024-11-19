import requests

# python -m pytest inventories_it.py
#200 -> update or receive , 201 -> create 

BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

#IT-auth-get-inventories

def test_add_inventory():

        inventory = {
        "id": 1,
        "item_id": "P000001",
        "description": "Face-to-face clear-thinking complexity",
        "item_reference": "sjQ23408K",
        "locations": [
            3211,
            24700,
            14123,
            19538,
            31071,
            24701,
            11606,
            11817
        ],
        "total_on_hand": 262,
        "total_expected": 0,
        "total_ordered": 80,
        "total_allocated": 41,
        "total_available": 141,
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
        }
        response = requests.post(f"{BASE_URL}/api/v1/inventories", json=inventory, headers=header)
        assert response.status_code == 201

def test_data_get_inventories():
        response = requests.get(f"{BASE_URL}/api/v1/inventories", headers=header)
        assert response.status_code == 200

def test_data_get_inventory():
        response = requests.get(f"{BASE_URL}/api/v1/inventories/1", headers=header)
        assert response.status_code == 200  


def test_update_inventory():
        inventory = {
        "id": 1,
        "item_id": "P000001",
        "description": "Face-to-face clear-thinking complexity updated",
        "item_reference": "sjQ23408K",
        "locations": [
            3211,
            24700,
            14123,
            19538,
            31071,
            24701,
            11606,
            11817
        ],
        "total_on_hand": 262,
        "total_expected": 0,
        "total_ordered": 80,
        "total_allocated": 41,
        "total_available": 141,
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
        }
        response = requests.put(f"{BASE_URL}/api/v1/inventories/1", json=inventory, headers=header)
        assert response.status_code == 200

def test_delete_inventory():
        response = requests.delete(f"{BASE_URL}/api/v1/inventories/1", headers=header)
        assert response.status_code == 200




# --------------------------- DOES NOT WORK ----------------------
# def test_get_inventories_for_item():
#           response = requests.get(f"{BASE_URL}/api/v1/inventories/{item_id}", headers=header)
#           assert response.status_code == 200

# def test_get_inventory_totals_for_item():
#          response = requests.get(f"{BASE_URL}/api/v1/inventories/item_idP000001", headers=header)
#          assert response.status_code == 200





