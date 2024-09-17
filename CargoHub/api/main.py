import socketserver
import http.server
import json

from providers import auth_provider
from providers import data_provider

from processors import notification_processor

class ApiRequestHandler(http.server.BaseHTTPRequestHandler):


    def handle_get_version_1(self, path, user):
        # Check if user has access to perform the "get" operation on the given path
        if not auth_provider.has_access(user, path, "get"):
            # Respond with a 403 Forbidden status if access is denied
            self.send_response(403)
            self.end_headers()
            return

        # Handle requests related to "warehouses"
        if path[0] == "warehouses":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all warehouses
                    warehouses = data_provider.fetch_warehouse_pool().get_warehouses()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouses).encode("utf-8"))
                case 2:
                    # Fetch and return specific warehouse by its ID
                    warehouse_id = int(path[1])
                    warehouse = data_provider.fetch_warehouse_pool().get_warehouse(warehouse_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouse).encode("utf-8"))
                case 3:
                    # Fetch and return all locations for a specific warehouse if "locations" is in the path
                    if path[2] == "locations":
                        warehouse_id = int(path[1])
                        locations = data_provider.fetch_location_pool().get_locations_in_warehouse(warehouse_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(locations).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "locations"
        elif path[0] == "locations":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all locations
                    locations = data_provider.fetch_location_pool().get_locations()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(locations).encode("utf-8"))
                case 2:
                    # Fetch and return a specific location by its ID
                    location_id = int(path[1])
                    location = data_provider.fetch_location_pool().get_location(location_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(location).encode("utf-8"))
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "transfers"
        elif path[0] == "transfers":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all transfers
                    transfers = data_provider.fetch_transfer_pool().get_transfers()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfers).encode("utf-8"))
                case 2:
                    # Fetch and return a specific transfer by its ID
                    transfer_id = int(path[1])
                    transfer = data_provider.fetch_transfer_pool().get_transfer(transfer_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfer).encode("utf-8"))
                case 3:
                    # Fetch and return items for a specific transfer if "items" is in the path
                    if path[2] == "items":
                        transfer_id = int(path[1])
                        items = data_provider.fetch_transfer_pool().get_items_in_transfer(transfer_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "items"
        elif path[0] == "items":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all items
                    items = data_provider.fetch_item_pool().get_items()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(items).encode("utf-8"))
                case 2:
                    # Fetch and return a specific item by its ID
                    item_id = int(path[1])
                    item = data_provider.fetch_item_pool().get_item(item_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item).encode("utf-8"))
                case 3:
                    # Fetch and return inventories for a specific item if "inventory" is in the path
                    if path[2] == "inventory":
                        item_id = int(path[1])
                        inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(item_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(inventories).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case 4:
                    # Fetch and return total inventories for a specific item if "inventory/totals" is in the path
                    if path[2] == "inventory" and path[3] == "totals":
                        item_id = int(path[1])
                        totals = data_provider.fetch_inventory_pool().get_inventory_totals_for_item(item_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(totals).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "item_lines"
        elif path[0] == "item_lines":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all item lines
                    item_lines = data_provider.fetch_item_line_pool().get_item_lines()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_lines).encode("utf-8"))
                case 2:
                    # Fetch and return a specific item line by its ID
                    item_line_id = int(path[1])
                    item_line = data_provider.fetch_item_line_pool().get_item_line(item_line_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_line).encode("utf-8"))
                case 3:
                    # Fetch and return items for a specific item line if "items" is in the path
                    if path[2] == "items":
                        item_line_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_line(item_line_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "item_groups"
        elif path[0] == "item_groups":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all item groups
                    item_groups = data_provider.fetch_item_group_pool().get_item_groups()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_groups).encode("utf-8"))
                case 2:
                    # Fetch and return a specific item group by its ID
                    item_group_id = int(path[1])
                    item_group = data_provider.fetch_item_group_pool().get_item_group(item_group_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_group).encode("utf-8"))
                case 3:
                    # Fetch and return items for a specific item group if "items" is in the path
                    if path[2] == "items":
                        item_group_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_group(item_group_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "item_types"
        elif path[0] == "item_types":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all item types
                    item_types = data_provider.fetch_item_type_pool().get_item_types()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_types).encode("utf-8"))
                case 2:
                    # Fetch and return a specific item type by its ID
                    item_type_id = int(path[1])
                    item_type = data_provider.fetch_item_type_pool().get_item_type(item_type_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_type).encode("utf-8"))
                case 3:
                    # Fetch and return items for a specific item type if "items" is in the path
                    if path[2] == "items":
                        item_type_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_type(item_type_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "inventories"
        elif path[0] == "inventories":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all inventories
                    inventories = data_provider.fetch_inventory_pool().get_inventories()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(inventories).encode("utf-8"))
                case 2:
                    # Fetch and return a specific inventory by its ID
                    inventory_id = int(path[1])
                    inventory = data_provider.fetch_inventory_pool().get_inventory(inventory_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(inventory).encode("utf-8"))
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "suppliers"
        elif path[0] == "suppliers":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all suppliers
                    suppliers = data_provider.fetch_supplier_pool().get_suppliers()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(suppliers).encode("utf-8"))
                case 2:
                    # Fetch and return a specific supplier by its ID
                    supplier_id = int(path[1])
                    supplier = data_provider.fetch_supplier_pool().get_supplier(supplier_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(supplier).encode("utf-8"))
                case 3:
                    # Fetch and return items for a specific supplier if "items" is in the path
                    if path[2] == "items":
                        supplier_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_supplier(supplier_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "orders"
        elif path[0] == "orders":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all orders
                    orders = data_provider.fetch_order_pool().get_orders()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(orders).encode("utf-8"))
                case 2:
                    # Fetch and return a specific order by its ID
                    order_id = int(path[1])
                    order = data_provider.fetch_order_pool().get_order(order_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(order).encode("utf-8"))
                case 3:
                    # Fetch and return items in a specific order if "items" is in the path
                    if path[2] == "items":
                        order_id = int(path[1])
                        items = data_provider.fetch_order_pool().get_items_in_order(order_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()

        # Handle requests related to "clients"
        elif path[0] == "clients":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return all clients
                    clients = data_provider.fetch_client_pool().get_clients()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(clients).encode("utf-8"))
                case 2:
                    # Fetch and return a specific client by its ID
                    client_id = int(path[1])
                    client = data_provider.fetch_client_pool().get_client(client_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(client).encode("utf-8"))
                case 3:
                    # Fetch and return orders for a specific client if "orders" is in the path
                    if path[2] == "orders":
                        client_id = int(path[1])
                        orders = data_provider.fetch_order_pool().get_orders_for_client(client_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(orders).encode("utf-8"))
                    else:
                        # Respond with 404 Not Found if the path is incorrect
                        self.send_response(404)
                        self.end_headers()
                case _:
                    # Respond with 404 Not Found for any other unmatched path length
                    self.send_response(404)
                    self.end_headers()
        # Handle requests related to "shipments"
        elif path[0] == "shipments":
            paths = len(path)
            match paths:
                case 1:  # Handle listing all shipments
                    shipments = data_provider.fetch_shipment_pool().get_shipments()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(shipments).encode("utf-8"))
                case 2:  # Handle fetching a specific shipment by ID
                    shipment_id = int(path[1])
                    shipment = data_provider.fetch_shipment_pool().get_shipment(shipment_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(shipment).encode("utf-8"))
                case 3:
                    if path[2] == "orders":  # Handle fetching orders within a shipment
                        shipment_id = int(path[1])
                        orders = data_provider.fetch_order_pool().get_orders_in_shipment(shipment_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(orders).encode("utf-8"))
                    elif path[2] == "items":  # Handle fetching items within a shipment
                        shipment_id = int(path[1])
                        items = data_provider.fetch_shipment_pool().get_items_in_shipment(shipment_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Send 404 Not Found if invalid path
                        self.end_headers()
                case _:
                    self.send_response(404)  # Send 404 Not Found for unsupported paths
                    self.end_headers()

        # Default response for unsupported top-level paths
        else:
            self.send_response(404)  # Send 404 Not Found for unsupported paths
            self.end_headers()

    def do_GET(self):
        api_key = self.headers.get("API_KEY")  # Fetch the API key from headers
        user = auth_provider.get_user(api_key)  # Get the user based on API key
        if user == None:  # If no valid user is found, send 401 Unauthorized
            self.send_response(401)
            self.end_headers()
        else:
            try:
                # Split the request path into parts
                path = self.path.split("/")
                # Check if the path is valid for API v1
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    # Call the handler for API v1 requests
                    self.handle_get_version_1(path[3:], user)
            except Exception:  # Handle any exceptions and send a 500 Internal Server Error response
                self.send_response(500)
                self.end_headers()

    # Handle POST requests for different paths in version 1 of the API
    def handle_post_version_1(self, path, user):
        # Check if the user has access rights to the requested path for POST
        if not auth_provider.has_access(user, path, "post"):
            self.send_response(403)  # Send 403 Forbidden response
            self.end_headers()
            return

        # Handle requests related to "warehouses"
        if path[0] == "warehouses":
            # Read the content length and data sent in the request body
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_warehouse = json.loads(post_data.decode())  # Parse JSON data
            # Add the new warehouse and save the changes
            data_provider.fetch_warehouse_pool().add_warehouse(new_warehouse)
            data_provider.fetch_warehouse_pool().save()
            self.send_response(201)  # Send 201 Created response
            self.end_headers()

        # Handle requests related to "locations"
        elif path[0] == "locations":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_location = json.loads(post_data.decode())
            # Add the new location and save the changes
            data_provider.fetch_location_pool().add_location(new_location)
            data_provider.fetch_location_pool().save()
            self.send_response(201)
            self.end_headers()

        # Handle requests related to "transfers"
        elif path[0] == "transfers":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_transfer = json.loads(post_data.decode())
            # Add the new transfer, save, and push a notification
            data_provider.fetch_transfer_pool().add_transfer(new_transfer)
            data_provider.fetch_transfer_pool().save()
            notification_processor.push(f"Scheduled batch transfer {new_transfer['id']}")
            self.send_response(201)
            self.end_headers()

        # Handle requests related to "items"
        elif path[0] == "items":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_item = json.loads(post_data.decode())
            # Add the new item and save the changes
            data_provider.fetch_item_pool().add_item(new_item)
            data_provider.fetch_item_pool().save()
            self.send_response(201)
            self.end_headers()

        # Handle requests related to "inventories"
        elif path[0] == "inventories":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_inventory = json.loads(post_data.decode())
            # Add the new inventory and save the changes
            data_provider.fetch_inventory_pool().add_inventory(new_inventory)
            data_provider.fetch_inventory_pool().save()
            self.send_response(201)
            self.end_headers()

        # Handle requests related to "suppliers"
        elif path[0] == "suppliers":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_supplier = json.loads(post_data.decode())
            # Add the new supplier and save the changes
            data_provider.fetch_supplier_pool().add_supplier(new_supplier)
            data_provider.fetch_supplier_pool().save()
            self.send_response(201)
            self.end_headers()

        # Handle requests related to "orders"
        elif path[0] == "orders":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_order = json.loads(post_data.decode())
            # Add the new order and save the changes
            data_provider.fetch_order_pool().add_order(new_order)
            data_provider.fetch_order_pool().save()
            self.send_response(201)
            self.end_headers()

        # Handle requests related to "clients"
        elif path[0] == "clients":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_client = json.loads(post_data.decode())
            # Add the new client and save the changes
            data_provider.fetch_client_pool().add_client(new_client)
            data_provider.fetch_client_pool().save()
            self.send_response(201)
            self.end_headers()

        # Handle requests related to "shipments"
        elif path[0] == "shipments":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_shipment = json.loads(post_data.decode())
            # Add the new shipment and save the changes
            data_provider.fetch_shipment_pool().add_shipment(new_shipment)
            data_provider.fetch_shipment_pool().save()
            self.send_response(201)
            self.end_headers()

        # Handle invalid path
        else:
            self.send_response(404)  # Send 404 Not Found if path is invalid
            self.end_headers()

    # Handle incoming POST requests
    def do_POST(self):
        api_key = self.headers.get("API_KEY")  # Fetch the API key from headers
        user = auth_provider.get_user(api_key)  # Get the user based on API key
        if user == None:  # If no valid user is found, send 401 Unauthorized
            self.send_response(401)
            self.end_headers()
        else:
            try:
                # Split the request path into parts
                path = self.path.split("/")
                # Check if the path is valid for API v1
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    # Call the handler for API v1 POST requests
                    self.handle_post_version_1(path[3:], user)
            except Exception:  # Handle any exceptions and send a 500 Internal Server Error response
                self.send_response(500)
                self.end_headers()

    # Handle PUT requests for different paths in version 1 of the API
    def handle_put_version_1(self, path, user):
        # Check if the user has access rights to the requested path for PUT
        if not auth_provider.has_access(user, path, "put"):
            self.send_response(403)  # Send 403 Forbidden response
            self.end_headers()
            return

        # Handle requests related to "warehouses"
        if path[0] == "warehouses":
            warehouse_id = int(path[1])  # Extract the warehouse ID from the path
            content_length = int(self.headers["Content-Length"])  # Get content length
            post_data = self.rfile.read(content_length)  # Read the request body
            updated_warehouse = json.loads(post_data.decode())  # Parse JSON data
            # Update the warehouse with the new data and save
            data_provider.fetch_warehouse_pool().update_warehouse(warehouse_id, updated_warehouse)
            data_provider.fetch_warehouse_pool().save()
            self.send_response(200)  # Send 200 OK response
            self.end_headers()

        # Handle requests related to "locations"
        elif path[0] == "locations":
            location_id = int(path[1])  # Extract the location ID from the path
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_location = json.loads(post_data.decode())  # Parse JSON data
            # Update the location and save
            data_provider.fetch_location_pool().update_location(location_id, updated_location)
            data_provider.fetch_location_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "transfers"
        elif path[0] == "transfers":
            paths = len(path)  # Get the number of elements in the path
            match paths:
                case 2:  # Update transfer details
                    transfer_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_transfer = json.loads(post_data.decode())
                    data_provider.fetch_transfer_pool().update_transfer(transfer_id, updated_transfer)
                    data_provider.fetch_transfer_pool().save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "commit":  # Commit transfer and update inventories
                        transfer_id = int(path[1])
                        transfer = data_provider.fetch_transfer_pool().get_transfer(transfer_id)
                        # Iterate through transfer items and update inventory totals
                        for x in transfer["items"]:
                            inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                            for y in inventories:
                                if y["location_id"] == transfer["transfer_from"]:
                                    # Adjust inventory at transfer from location
                                    y["total_on_hand"] -= x["amount"]
                                    y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                                    y["total_available"] = y["total_on_hand"] - y["total_allocated"]
                                    data_provider.fetch_inventory_pool().update_inventory(y["id"], y)
                                elif y["location_id"] == transfer["transfer_to"]:
                                    # Adjust inventory at transfer to location
                                    y["total_on_hand"] += x["amount"]
                                    y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                                    y["total_available"] = y["total_on_hand"] - y["total_allocated"]
                                    data_provider.fetch_inventory_pool().update_inventory(y["id"], y)
                        transfer["transfer_status"] = "Processed"  # Update transfer status to processed
                        data_provider.fetch_transfer_pool().update_transfer(transfer_id, transfer)
                        notification_processor.push(f"Processed batch transfer with id:{transfer['id']}")  # Send notification
                        data_provider.fetch_transfer_pool().save()
                        data_provider.fetch_inventory_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    else:
                        self.send_response(404)  # Send 404 if invalid path
                        self.end_headers()
                case _:
                    self.send_response(404)  # Send 404 if invalid path
                    self.end_headers()

        # Handle requests related to "items"
        elif path[0] == "items":
            item_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item = json.loads(post_data.decode())
            data_provider.fetch_item_pool().update_item(item_id, updated_item)
            data_provider.fetch_item_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "item_lines"
        elif path[0] == "item_lines":
            item_line_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item_line = json.loads(post_data.decode())
            data_provider.fetch_item_line_pool().update_item_line(item_line_id, updated_item_line)
            data_provider.fetch_item_line_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "item_groups"
        elif path[0] == "item_groups":
            item_group_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item_group = json.loads(post_data.decode())
            data_provider.fetch_item_group_pool().update_item_group(item_group_id, updated_item_group)
            data_provider.fetch_item_group_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "item_types"
        elif path[0] == "item_types":
            item_type_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item_type = json.loads(post_data.decode())
            data_provider.fetch_item_type_pool().update_item_type(item_type_id, updated_item_type)
            data_provider.fetch_item_type_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "inventories"
        elif path[0] == "inventories":
            inventory_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_inventory = json.loads(post_data.decode())
            data_provider.fetch_inventory_pool().update_inventory(inventory_id, updated_inventory)
            data_provider.fetch_inventory_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "suppliers"
        elif path[0] == "suppliers":
            supplier_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_supplier = json.loads(post_data.decode())
            data_provider.fetch_supplier_pool().update_supplier(supplier_id, updated_supplier)
            data_provider.fetch_supplier_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "orders"
        elif path[0] == "orders":
            paths = len(path)
            match paths:
                case 2:  # Update order details
                    order_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_order = json.loads(post_data.decode())
                    data_provider.fetch_order_pool().update_order(order_id, updated_order)
                    data_provider.fetch_order_pool().save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "items":  # Update items in the order
                        order_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_items = json.loads(post_data.decode())
                        data_provider.fetch_order_pool().update_items_in_order(order_id, updated_items)
                        data_provider.fetch_order_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    else:
                        self.send_response(404)  # Send 404 if invalid path
                        self.end_headers()
                case _:
                    self.send_response(404)  # Send 404 if invalid path
                    self.end_headers()

        # Handle requests related to "clients"
        elif path[0] == "clients":
            client_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_client = json.loads(post_data.decode())
            data_provider.fetch_client_pool().update_client(client_id, updated_client)
            data_provider.fetch_client_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "shipments"
        elif path[0] == "shipments":
            paths = len(path)
            match paths:
                case 2:  # Update shipment details
                    shipment_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_shipment = json.loads(post_data.decode())
                    data_provider.fetch_shipment_pool().update_shipment(shipment_id, updated_shipment)
                    data_provider.fetch_shipment_pool().save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "orders":  # Update orders in the shipment
                        shipment_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_orders = json.loads(post_data.decode())
                        data_provider.fetch_order_pool().update_orders_in_shipment(shipment_id, updated_orders)
                        data_provider.fetch_order_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    elif path[2] == "items":  # Update items in the shipment
                        shipment_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_items = json.loads(post_data.decode())
                        data_provider.fetch_shipment_pool().update_items_in_shipment(shipment_id, updated_items)
                        data_provider.fetch_shipment_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    elif path[2] == "commit":  # Logic to commit shipment (left as 'pass')
                        pass
                    else:
                        self.send_response(404)  # Send 404 if invalid path
                        self.end_headers()
                case _:
                    self.send_response(404)  # Send 404 if invalid path
                    self.end_headers()

        # Handle invalid path
        else:
            self.send_response(404)  # Send 404 Not Found if path is invalid
            self.end_headers()

    # Handle incoming PUT requests
    def do_PUT(self):
        api_key = self.headers.get("API_KEY")  # Fetch the API key from headers
        user = auth_provider.get_user(api_key)  # Get the user based on API key
        if user == None:  # If no valid user is found, send 401 Unauthorized
            self.send_response(401)
            self.end_headers()
        else:
            try:
                # Split the request path into parts
                path = self.path.split("/")
                # Check if the path is valid for API v1
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    # Call the handler for API v1 PUT requests
                    self.handle_put_version_1(path[3:], user)
            except Exception:  # Handle any exceptions and send a 500 Internal Server Error response
                self.send_response(500)
                self.end_headers()

    # Handle DELETE requests for version 1 of the API
    def handle_delete_version_1(self, path, user):
        # Check if the user has access rights to the requested path for DELETE
        if not auth_provider.has_access(user, path, "delete"):
            self.send_response(403)  # Send 403 Forbidden response
            self.end_headers()
            return

        # Handle requests related to "warehouses"
        if path[0] == "warehouses":
            warehouse_id = int(path[1])  # Extract the warehouse ID from the path
            # Remove the warehouse and save the changes
            data_provider.fetch_warehouse_pool().remove_warehouse(warehouse_id)
            data_provider.fetch_warehouse_pool().save()
            self.send_response(200)  # Send 200 OK response
            self.end_headers()

        # Handle requests related to "locations"
        elif path[0] == "locations":
            location_id = int(path[1])  # Extract the location ID from the path
            # Remove the location and save the changes
            data_provider.fetch_location_pool().remove_location(location_id)
            data_provider.fetch_location_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "transfers"
        elif path[0] == "transfers":
            transfer_id = int(path[1])  # Extract the transfer ID from the path
            # Remove the transfer and save the changes
            data_provider.fetch_transfer_pool().remove_transfer(transfer_id)
            data_provider.fetch_transfer_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "items"
        elif path[0] == "items":
            item_id = int(path[1])  # Extract the item ID from the path
            # Remove the item and save the changes
            data_provider.fetch_item_pool().remove_item(item_id)
            data_provider.fetch_item_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "item_lines"
        elif path[0] == "item_lines":
            item_line_id = int(path[1])  # Extract the item line ID from the path
            # Remove the item line and save the changes
            data_provider.fetch_item_line_pool().remove_item_line(item_line_id)
            data_provider.fetch_item_line_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "item_groups"
        elif path[0] == "item_groups":
            item_group_id = int(path[1])  # Extract the item group ID from the path
            # Remove the item group and save the changes
            data_provider.fetch_item_group_pool().remove_item_group(item_group_id)
            data_provider.fetch_item_group_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "item_types"
        elif path[0] == "item_types":
            item_type_id = int(path[1])  # Extract the item type ID from the path
            # Remove the item type and save the changes
            data_provider.fetch_item_type_pool().remove_item_type(item_type_id)
            data_provider.fetch_item_type_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "inventories"
        elif path[0] == "inventories":
            inventory_id = int(path[1])  # Extract the inventory ID from the path
            # Remove the inventory and save the changes
            data_provider.fetch_inventory_pool().remove_inventory(inventory_id)
            data_provider.fetch_inventory_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "suppliers"
        elif path[0] == "suppliers":
            supplier_id = int(path[1])  # Extract the supplier ID from the path
            # Remove the supplier and save the changes
            data_provider.fetch_supplier_pool().remove_supplier(supplier_id)
            data_provider.fetch_supplier_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "orders"
        elif path[0] == "orders":
            order_id = int(path[1])  # Extract the order ID from the path
            # Remove the order and save the changes
            data_provider.fetch_order_pool().remove_order(order_id)
            data_provider.fetch_order_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "clients"
        elif path[0] == "clients":
            client_id = int(path[1])  # Extract the client ID from the path
            # Remove the client and save the changes
            data_provider.fetch_client_pool().remove_client(client_id)
            data_provider.fetch_client_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle requests related to "shipments"
        elif path[0] == "shipments":
            shipment_id = int(path[1])  # Extract the shipment ID from the path
            # Remove the shipment and save the changes
            data_provider.fetch_shipment_pool().remove_shipment(shipment_id)
            data_provider.fetch_shipment_pool().save()
            self.send_response(200)
            self.end_headers()

        # Handle invalid path
        else:
            self.send_response(404)  # Send 404 Not Found if the path is invalid
            self.end_headers()

    # Handle incoming DELETE requests
    def do_DELETE(self):
        api_key = self.headers.get("API_KEY")  # Fetch the API key from headers
        user = auth_provider.get_user(api_key)  # Get the user based on the API key
        if user is None:  # If no valid user is found, send 401 Unauthorized
            self.send_response(401)
            self.end_headers()
        else:
            try:
                # Split the request path into parts
                path = self.path.split("/")
                # Check if the path is valid for API v1
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    # Call the handler for API v1 DELETE requests
                    self.handle_delete_version_1(path[3:], user)
            except Exception:  # Handle any exceptions and send a 500 Internal Server Error
                self.send_response(500)
                self.end_headers()

# Main server block
if __name__ == "__main__":
    PORT = 3000  # Define the port to run the server
    # Initialize and run the server using TCPServer
    with socketserver.TCPServer(("", PORT), ApiRequestHandler) as httpd:
        auth_provider.init()  # Initialize the authentication provider
        data_provider.init()  # Initialize the data provider
        notification_processor.start()  # Start the notification processor
        print(f"Serving on port {PORT}...")  # Output the server status
        httpd.serve_forever()  # Start serving requests indefinitely