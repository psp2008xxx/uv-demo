from utils.models import Order


class StoreAPI:
    def __init__(self, client):
        self.client = client

    def get_inventory(self):
        url = "/store/inventory"
        response = self.client.get(endpoint=url)
        return response

    def place_order(self, order_data):
        order = Order(**order_data)  # Validate input
        url = "/store/order"
        response = self.client.post(endpoint=url, json=order.model_dump())
        return response

    def get_order_by_id(self, order_id):
        url = f"/store/order/{order_id}"
        response = self.client.get(endpoint=url)
        if response.status_code == 200:
            Order(**response.json())  # Validate response
        return response

    def delete_order(self, order_id):
        url = f"/store/order/{order_id}"
        response = self.client.delete(endpoint=url)
        return response
