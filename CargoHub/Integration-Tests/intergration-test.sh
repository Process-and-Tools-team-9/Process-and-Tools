#!/bin/bash
python -m pytest clients_it.py
python -m pytest inventories_it.py
python -m pytest item_groups_it.py
python -m pytest item_lines_it.py
python -m pytest item_types_it.py
python -m pytest items_it.py
python -m pytest locations_it.py
python -m pytest orders_it.py
python -m pytest shipments_it.py
python -m pytest suppliers_it.py 
python -m pytest transfers_it.py
python -m pytest warehouses_it.py