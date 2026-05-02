import pytest
import os

from utils.yaml_loader import load_yaml



cases = load_yaml(os.path.join(os.path.dirname(__file__), '../testdata/pet/get_pet.yaml'))['cases']


@pytest.mark.parametrize('cases', cases)
def test_get_pet_by_id(cases, pet_service):
    response = pet_service.get_pet_by_id(cases['pet_id'])
    assert response.status_code == cases['expected_status']
    if response.status_code == 200:
        assert response.json()["id"] == cases['pet_id']
    else:
        assert response.json()["type"] == cases['expected_type']
        assert response.json()["code"] == cases['expected_code']


def test_get_pet_status(pet_service, status):
    response = pet_service.get_pets_by_status(status)
    assert response.status_code == 200
    for pet in response.json():
        assert pet["status"] == status
