import requests

# python -m pytest orders_it.py
# 200 -> update or receive , 201 -> create 

BASE_URL = "http://localhost:3000"
header = {"api_key": "a1b2c3d4e5"}

# IT-auth-get-orders

def test_create_order():
    order = {
        "id": 1,
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "ship_to": None,
        "bill_to": None,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
        "created_at": "2019-04-03T11:33:15Z",
        "updated_at": "2019-04-05T07:33:15Z",
        "items": [
            {"item_id": "P007435", "amount": 23},
            {"item_id": "P009557", "amount": 1},
            {"item_id": "P009553", "amount": 50}
        ]
    }
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=order, headers=header)
    assert response.status_code == 201

def test_get_orders():
    response = requests.get(f"{BASE_URL}/api/v1/orders", headers=header)
    assert response.status_code == 200

def test_get_order():
    order_id = 1
    response = requests.get(f"{BASE_URL}/api/v1/orders/{order_id}", headers=header)
    assert response.status_code == 200

def test_update_order():
    updated_order = {
        "id": 1,
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Updated reference details.",
        "order_status": "Pending",
        "notes": "Updated order notes.",
        "shipping_notes": "Updated shipping instructions.",
        "picking_notes": "Updated picking notes.",
        "warehouse_id": 18,
        "ship_to": None,
        "bill_to": None,
        "shipment_id": 1,
        "total_amount": 9800.00,
        "total_discount": 200.00,
        "total_tax": 350.00,
        "total_surcharge": 50.00,
        "created_at": "2019-04-03T11:33:15Z",
        "updated_at": "2024-11-19T15:00:00Z",
        "items": [
            {"item_id": "P007435", "amount": 20},
            {"item_id": "P009557", "amount": 2}
        ]
    }
    response = requests.put(f"{BASE_URL}/api/v1/orders/1", json=updated_order, headers=header)
    assert response.status_code == 200

def test_delete_order():
    order_id = 1
    response = requests.delete(f"{BASE_URL}/api/v1/orders/{order_id}", headers=header)
    assert response.status_code == 200
