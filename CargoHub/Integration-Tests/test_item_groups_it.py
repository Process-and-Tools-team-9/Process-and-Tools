import requests

# python -m pytest item_groups_it.py
# 200 -> update or receive , 201 -> create 

BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

# IT-auth-get-item-groups


item_group = {
        "id": 0,
        "name": "Electronics",
        "description": "Group for electronic items",
        "created_at": "1998-05-15 19:52:53",
        "updated_at": "2000-11-20 08:37:56"
    }


def test_get_item_groups():
    response = requests.get(f"{BASE_URL}/api/v1/item_groups", headers=header)
    assert response.status_code == 200

def test_get_item_group():
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/1", headers=header)
    assert response.status_code == 200

def test_update_item_group():
    updated_item_group = {
        "id": 1,
        "name": "Updated Electronics",
        "description": "Updated description for electronic items",
        "created_at": "1998-05-15 19:52:53",
        "updated_at": "2024-11-19 10:00:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_groups/1", json=updated_item_group, headers=header)
    assert response.status_code == 200

def test_delete_item_group():
    response = requests.delete(f"{BASE_URL}/api/v1/item_groups/1", headers=header)
    assert response.status_code == 200
