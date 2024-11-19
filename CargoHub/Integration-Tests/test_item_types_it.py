import requests

# python -m pytest item_types_it.py
# 200 -> update or receive , 201 -> create 

BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

# IT-auth-get-item-types


item_type = {
        "id": 0,
        "name": "Gadgets",
        "description": "Category for small electronic devices",
        "created_at": "2010-03-10 12:00:00",
        "updated_at": "2010-03-15 14:00:00"
    }

def test_get_item_types():
    response = requests.get(f"{BASE_URL}/api/v1/item_types", headers=header)
    assert response.status_code == 200

def test_get_item_type():
    response = requests.get(f"{BASE_URL}/api/v1/item_types/1", headers=header)
    assert response.status_code == 200

def test_update_item_type():
    updated_item_type = {
        "id": 1,
        "name": "Updated Gadgets",
        "description": "Updated category for small electronic devices",
        "created_at": "2010-03-10 12:00:00",
        "updated_at": "2024-11-19 10:15:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_types/1", json=updated_item_type, headers=header)
    assert response.status_code == 200

def test_delete_item_type():
    response = requests.delete(f"{BASE_URL}/api/v1/item_types/1", headers=header)
    assert response.status_code == 200
