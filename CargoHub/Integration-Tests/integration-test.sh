#!/bin/bash

cd "$(dirname "$0")"

python -m pytest test_clients_it.py
python -m pytest test_inventories_it.py
python -m pytest test_item_groups_it.py
python -m pytest test_item_lines_it.py
python -m pytest test_item_types_it.py
python -m pytest test_items_it.py
python -m pytest test_locations_it.py
python -m pytest test_orders_it.py
python -m pytest test_shipments_it.py
python -m pytest test_suppliers_it.py 
python -m pytest test_transfers_it.py
python -m pytest test_warehouses_it.py