import requests

# python -m pytest locations_it.py


BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

def test_add_location():

    location = {
        "id": 2,
        "warehouse_id": 1,
        "code": "A.1.1",
        "name": "Row: A, Rack: 1, Shelf: 1",
        "created_at": "1992-05-15 03:21:32",
        "updated_at": "1992-05-15 03:21:32"
    }
    response = requests.post(f"{BASE_URL}/api/v1/locations", json=location, headers=header)
    assert response.status_code == 201

def test_get_locations():
    response = requests.get(f"{BASE_URL}/api/v1/locations", headers=header)
    assert response.status_code == 200

def test_get_warehouse():
    response = requests.get(f"{BASE_URL}/api/v1/locations/2", headers=header)
    assert response.status_code == 200



def test_update_location():

    location = {
        "id": 2,
        "warehouse_id": 1,
        "code": "A.1.1",
        "name": "Row: A, Rack: 1, Shelf: 1_updated",
        "created_at": "1992-05-15 03:21:32",
        "updated_at": "1992-05-15 03:21:32"
    }
    response = requests.put(f"{BASE_URL}/api/v1/locations/2", json=location, headers=header)
    assert response.status_code == 200

def test_delete_location():
    response = requests.delete(f"{BASE_URL}/api/v1/locations/2", headers=header)
    assert response.status_code == 200

## -- Werkt niet

# def test_get_locations_in_warehouse():
#     response = requests.get(f"{BASE_URL}/api/v1/locations/warehouse/2", headers=header)
#     assert response.status_code == 200


