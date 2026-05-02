import pytest
import os
from api.pet_api import PetAPI
from utils.yaml_loader import load_yaml
from client.http_client import HttpClient
from faker import Faker


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="select testing environment: dev / test / prod")


@pytest.fixture(scope="session")
def config(pytestconfig):
    env = pytestconfig.getoption("env")
    config_path = os.path.join("config", f"{env}.yaml")
    return load_yaml(config_path)


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="session")
def status(config):
    return config["status"]


@pytest.fixture(scope="session")
def client(base_url):
    return HttpClient(base_url)


@pytest.fixture
def pet_service(client):
    return PetAPI(client)


@pytest.fixture
def store_service(client):
    from api.store_api import StoreAPI
    return StoreAPI(client)


@pytest.fixture
def user_service(client):
    from api.user_api import UserAPI
    return UserAPI(client)


fake = Faker()


@pytest.fixture
def random_pet():
    return {
        "name": fake.name(),
        "photoUrls": [fake.image_url()],
        "status": "available"
    }


@pytest.fixture
def random_user():
    return {
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number()
    }


@pytest.fixture
def random_order():
    return {
        "petId": fake.random_int(min=1, max=100),
        "quantity": fake.random_int(min=1, max=10),
        "status": "placed",
        "complete": False
    }
