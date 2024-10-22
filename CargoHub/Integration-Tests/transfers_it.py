import requests
import json

# python -m pytest transfers_it.py

BASE_URL = "http://localhost:3000/api/v1"
header = {"api_key": "a1b2c3d4e5"}

transfer = {
    "id": 1,
    "reference": "TR00001",
    "transfer_from": None,
    "transfer_to": 9229,
    "transfer_status": "Completed",
    "created_at": "2000-03-11T13:11:14Z",
    "updated_at": "2000-03-12T16:11:14Z",
    "items": [
        {
            "item_id": "P007435",
            "amount": 23
        }
    ]
}

#### TESTS ####

def test_get_all_transfers():
    response = requests.get(f"{BASE_URL}/transfers", headers=header)
    assert response.status_code == 200

def test_get_transfer_by_id():
    response = requests.get(f"{BASE_URL}/transfers/1", headers=header)
    assert response.status_code == 200

def test_create_transfer():
    response = requests.post(f"{BASE_URL}/transfers", json=transfer, headers=header)
    assert response.status_code == 201

def test_update_transfer():
    updated_transfer = transfer.copy()
    updated_transfer["transfer_status"] = "In Progress"
    response = requests.put(f"{BASE_URL}/transfers/1", json=updated_transfer, headers=header)
    assert response.status_code == 200

def test_delete_transfer():
    response = requests.delete(f"{BASE_URL}/transfers/1", headers=header)
    assert response.status_code == 200