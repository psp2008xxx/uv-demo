import pytest


def test_get_inventory(store_service):
    response = store_service.get_inventory()
    assert response.status_code == 200
    # Assuming inventory is a dict with status counts
    assert isinstance(response.json(), dict)


def test_place_and_get_order(store_service, random_order):
    # Place order
    response = store_service.place_order(random_order)
    assert response.status_code == 200
    order = response.json()
    order_id = order['id']

    # Get order
    response = store_service.get_order_by_id(order_id)
    assert response.status_code == 200
    retrieved_order = response.json()
    assert retrieved_order['id'] == order_id

    # Delete order
    response = store_service.delete_order(order_id)
    assert response.status_code == 200


def test_delete_nonexistent_order(store_service):
    response = store_service.delete_order(99999)
    assert response.status_code == 404
