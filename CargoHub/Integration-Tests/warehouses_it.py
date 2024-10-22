import requests

# python -m pytest warehouses_it.py

BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

# Integration test -> add a warehouse
def test_add_warehouse():
    
    warehouse = {
        "id": 2,
        "code": "GIOMNL90",
        "name": "Petten longterm hub",
        "address": "Owenweg 731",
        "zip": "4615 RB",
        "city": "Petten",
        "province": "Noord-Holland",
        "country": "NL",
        "contact": {
            "name": "Maud Adryaens",
            "phone": "+31836 752702",
            "email": "nickteunissen@example.com"
        },
        "created_at": "2008-02-22 19:55:39",
        "updated_at": "2009-08-28 23:15:50"
    }
    response = requests.post(f"{BASE_URL}/api/v1/warehouses", json=warehouse, headers=header)
    assert response.status_code == 201

# Integration test -> get all warehouses
def test_get_warehouses():
    response = requests.get(f"{BASE_URL}/api/v1/warehouses", headers=header)
    assert response.status_code == 200

# Integration test -> get a warehouse
def test_get_warehouse():
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/2", headers=header)
    assert response.status_code == 200

# Inegration test -> update a warehouse
def test_update_warehouse():
    warehouse = {
        "id": 2,
        "code": "GIOMNL90",
        "name": "Petten longterm hub updated version",
        "address": "Owenweg 731",
        "zip": "4615 RB",
        "city": "Petten",
        "province": "Noord-Holland",
        "country": "NL",
        "contact": {
            "name": "Maud Adryaens",
            "phone": "+31836 752702",
            "email": "nickteunissen@example.com"
        },
        "created_at": "2024-10-14T09:53:50.589800Z",
        "updated_at": "2024-10-14T09:53:50.589800Z"
    }
    response = requests.put(f"{BASE_URL}/api/v1/warehouses/2", json=warehouse, headers=header)
    assert response.status_code == 200

# Integration test -> delete a warehouse by id
def test_delete_inventory():
    response = requests.delete(f"{BASE_URL}/api/v1/warehouses/2", headers=header)
    assert response.status_code == 200