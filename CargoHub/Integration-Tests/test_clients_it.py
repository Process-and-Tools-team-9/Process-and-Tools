import requests

# python -m pytest clients_it.py
#200 -> update or receive, 201 -> create

BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

#IT-auth-get-clients

def test_add_client():
    client = {"id": 1, "name": "Raymond Inc", "address": "1296 Daniel Road Apt. 349", "city": "Pierceview", "zip_code": "28301", "province": "Colorado", "country": "United States", "contact_name": "Bryan Clark", "contact_phone": "242.732.3483x2573", "contact_email": "robertcharles@example.net", "created_at": "2010-04-28 02:22:53", "updated_at": "2022-02-09 20:22:35"}
    response = requests.post(f"{BASE_URL}/api/v1/clients", json=client, headers=header)
    assert response.status_code == 201

def test_data_get_clients():
    response = requests.get(f"{BASE_URL}/api/v1/clients", headers=header)
    assert response.status_code == 200

def test_data_get_client():
    response = requests.get(f"{BASE_URL}/api/v1/clients/1", headers=header)
    assert response.status_code == 200

def test_update_client():
    client = {"id": 1, "name": "Raymond Inc", "address": "1296 Daniel Road Apt. 349", "city": "Pierceview", "zip_code": "28301", "province": "Colorado", "country": "United States", "contact_name": "Bryan Clark", "contact_phone": "242.732.3483x2573", "contact_email": "robertcharles@example.net", "created_at": "2010-04-28 02:22:53", "updated_at": "2022-02-09 20:22:35"}
    response = requests.post(f"{BASE_URL}/api/v1/clients", json=client, headers=header)
    assert response.status_code == 201


def test_delete_client():
        response = requests.delete(f"{BASE_URL}/api/v1/clients/1", headers=header)
        assert response.status_code == 200
