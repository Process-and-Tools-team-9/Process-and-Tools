import requests

# python -m pytest shipments_it.py
#200 -> update or receive , 201 -> create 

BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

def test_add_shipment():
    inventory = {
        "id": 1,
        "order_id": 1,
        "source_id": 33,
        "order_date": "2000-03-09",
        "request_date": "2000-03-11",
        "shipment_date": "2000-03-13",
        "shipment_type": "I",
        "shipment_status": "Pending",
        "notes": "Zee vertrouwen klas rots heet lachen oneven begrijpen.",
        "carrier_code": "DPD",
        "carrier_description": "Dynamic Parcel Distribution",
        "service_code": "Fastest",
        "payment_type": "Manual",
        "transfer_mode": "Ground",
        "total_package_count": 31,
        "total_package_weight": 594.42,
        "created_at": "2000-03-10T11:11:14Z",
        "updated_at": "2000-03-11T13:11:14Z",
        "items": [
            {"item_id": "P007435", "amount": 23},
            {"item_id": "P009557", "amount": 1},
            {"item_id": "P009553", "amount": 50},
            {"item_id": "P010015", "amount": 16},
            {"item_id": "P002084", "amount": 33},
            {"item_id": "P009663", "amount": 18},
            {"item_id": "P010125", "amount": 18},
            {"item_id": "P005768", "amount": 26},
            {"item_id": "P004051", "amount": 1},
            {"item_id": "P005026", "amount": 29},
            {"item_id": "P000726", "amount": 22},
            {"item_id": "P008107", "amount": 47},
            {"item_id": "P001598", "amount": 32},
            {"item_id": "P002855", "amount": 20},
            {"item_id": "P010404", "amount": 30},
            {"item_id": "P010446", "amount": 6},
            {"item_id": "P001517", "amount": 9},
            {"item_id": "P009265", "amount": 2},
            {"item_id": "P001108", "amount": 20},
            {"item_id": "P009110", "amount": 18},
            {"item_id": "P009686", "amount": 13}
        ]}
    response = requests.post(f"{BASE_URL}/api/v1/shipments", json=inventory, headers=header)
    assert response.status_code == 201

def test_data_get_shipments():
    response = requests.get(f"{BASE_URL}/api/v1/shipments", headers=header)
    assert response.status_code == 200

def test_data_get_shipment():
    response = requests.get(f"{BASE_URL}/api/v1/shipments/1", headers=header)
    assert response.status_code == 200

def test_data_get_items_in_shipment():
    response = requests.get(f"{BASE_URL}/api/v1/shipments/1/items", headers=header)
    assert response.status_code == 200

def test_update_shipments():
    updated_shipment = {
        "id": 1,
        "order_id": 1,
        "source_id": 33,
        "order_date": "2000-03-09",
        "request_date": "2000-03-11",
        "shipment_date": "2000-03-13",
        "shipment_type": "I",
        "shipment_status": "Shipped",  # Change status for testing
        "notes": "Updated status.",
        "carrier_code": "DPD",
        "carrier_description": "Dynamic Parcel Distribution",
        "service_code": "Fastest",
        "payment_type": "Manual",
        "transfer_mode": "Ground",
        "total_package_count": 31,
        "total_package_weight": 594.42,
        "created_at": "2000-03-10T11:11:14Z",
        "updated_at": "2000-03-11T13:11:14Z",
        "items": [
            {"item_id": "P007435", "amount": 23},
            {"item_id": "P009557", "amount": 1},
            {"item_id": "P009553", "amount": 50},
            {"item_id": "P010015", "amount": 16},
            {"item_id": "P002084", "amount": 33},
            {"item_id": "P009663", "amount": 18},
            {"item_id": "P010125", "amount": 18},
            {"item_id": "P005768", "amount": 26},
            {"item_id": "P004051", "amount": 1},
            {"item_id": "P005026", "amount": 29},
            {"item_id": "P000726", "amount": 22},
            {"item_id": "P008107", "amount": 47},
            {"item_id": "P001598", "amount": 32},
            {"item_id": "P002855", "amount": 20},
            {"item_id": "P010404", "amount": 30},
            {"item_id": "P010446", "amount": 6},
            {"item_id": "P001517", "amount": 9},
            {"item_id": "P009265", "amount": 2},
            {"item_id": "P001108", "amount": 20},
            {"item_id": "P009110", "amount": 18},
            {"item_id": "P009686", "amount": 13}
        ]}
    response = requests.put(f"{BASE_URL}/api/v1/shipments/1", json=updated_shipment, headers=header)
    assert response.status_code == 200

def test_remove_shipment():
    response = requests.delete(f"{BASE_URL}/api/v1/shipments/1", headers=header)
    assert response.status_code == 200

