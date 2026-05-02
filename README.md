# UV-Demo: Petstore API Testing Framework

A comprehensive Python-based testing framework for the Swagger Petstore API, built with Pytest, Pydantic, and Requests.

## Features

- **Full API Coverage**: Implements all Petstore endpoints (pets, store, users).
- **Schema Validation**: Uses Pydantic models for request/response validation.
- **Dynamic Test Data**: Generates random test data with Faker.
- **HTTP Client**: Custom client with logging, sessions, and timeouts.
- **Reporting**: HTML reports via pytest-html.
- **Configuration**: Environment-based config (dev/prod).

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Run tests:
   ```bash
   pytest tests/ --html=report.html
   ```

3. Switch environments:
   ```bash
   pytest --env=prod tests/
   ```

## Structure

- `api/`: API service classes (PetAPI, StoreAPI, UserAPI).
- `client/`: HTTP client with session management.
- `utils/`: Models, logger, YAML loader.
- `tests/`: Test cases with fixtures.
- `config/`: Environment configurations.

## Usage

Use fixtures in tests:
```python
def test_add_pet(pet_service, random_pet):
    response = pet_service.add_pet(random_pet)
    assert response.status_code == 200
```

## Enhancements

- Schema validation ensures data integrity.
- File uploads supported in HttpClient.
- Comprehensive test suite for all APIs.
