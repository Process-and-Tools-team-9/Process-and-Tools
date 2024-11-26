#!/bin/bash


cd "$(dirname "$0")"


# python -m pytest \
#     --cov=CargoHub/api \
#     --cov-report=xml:coverage.xml \
#     --cov-report=term \
#     test_clients_it.py \
#     test_inventories_it.py \
#     test_item_groups_it.py \
#     test_item_lines_it.py \
#     test_item_types_it.py \
#     test_items_it.py \
#     test_locations_it.py \
#     test_orders_it.py \
#     test_shipments_it.py \
#     test_suppliers_it.py \
#     test_transfers_it.py \
#     test_warehouses_it.py

# # Check the exit status of pytest
# if [ $? -ne 0 ]; then
#     echo "Integration tests failed!"
#     exit 1
# fi

# echo "Integration tests completed successfully. Coverage report generated at coverage.xml"


#zonder code coverage.
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
