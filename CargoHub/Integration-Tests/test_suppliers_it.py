import requests

#  python -m pytest suppliers_it.py 


BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

def test_add_supplier():

    supplier = {
        "id": 3,
        "code": "SUP0003",
        "name": "White and Sons",
        "address": "1761 Shepard Valley",
        "address_extra": "Suite 853",
        "city": "Aguilarton",
        "zip_code": "63918",
        "province": "Wyoming",
        "country": "Ghana",
        "contact_name": "Jason Hudson",
        "phonenumber": "001-910-585-6962x8307",
        "reference": "WaS-SUP0003",
        "created_at": "2010-06-14 02:32:58",
        "updated_at": "2019-06-16 19:29:49"
    }
    response = requests.post(f"{BASE_URL}/api/v1/suppliers", json=supplier, headers=header)
    assert response.status_code == 201

def test_get_supplliers():
    response = requests.get(f"{BASE_URL}/api/v1/suppliers", headers=header)
    assert response.status_code == 200

def test_get_supplier():
    response = requests.get(f"{BASE_URL}/api/v1/suppliers/3", headers=header) 
    assert response.status_code == 200

def test_update_supplier():
    supplier = {
                "id": 3,
        "code": "SUP0003",
        "name": "White and Sons updated version",
        "address": "1761 Shepard Valley",
        "address_extra": "Suite 853",
        "city": "Aguilarton",
        "zip_code": "63918",
        "province": "Wyoming",
        "country": "Ghana",
        "contact_name": "Jason Hudson",
        "phonenumber": "001-910-585-6962x8307",
        "reference": "WaS-SUP0003",
        "created_at": "2024-10-22T13:24:54.851843Z",
        "updated_at": "2024-10-22T13:24:54.851843Z"
    }

    response = requests.put(f"{BASE_URL}/api/v1/suppliers/3", json=supplier, headers=header)
    assert response.status_code == 200

def test_delete_supplier():
    response = requests.delete(f"{BASE_URL}/api/v1/suppliers/3", headers=header)
    assert response.status_code == 200