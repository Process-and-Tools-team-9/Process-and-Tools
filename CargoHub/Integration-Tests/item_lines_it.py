import requests

# python -m pytest item_lines_it.py

# TODO: replace with test server url
BASE_URL = "http://localhost:3000/api/v1"
header = {"api_key": "a1b2c3d4e5"}

item_line = {
    "id": 0,
    "name": "Tech Gadgets2",
    "description": "",
    "created_at": "2022-08-18 07:05:25",
    "updated_at": "2023-05-15 15:44:28"
}


#### TESTS ####

def test_get_all_item_lines():
    response = requests.get(f"{BASE_URL}/item_lines", headers=header)
    assert response.status_code == 200


def test_get_item_line_by_id():
    response = requests.get(f"{BASE_URL}/item_lines/1", headers=header)
    assert response.status_code == 200

##### DOES NOT WORK
#### CLEARS THE JSON FOR SOME REASON
def test_update_item_line():
    response = requests.put(f"{BASE_URL}/item_lines/0", json=item_line, headers=header)
    assert response.status_code == 200


def test_delete_item_line():
    response = requests.delete(f"{BASE_URL}/item_lines/0", headers=header)
    assert response.status_code == 200


