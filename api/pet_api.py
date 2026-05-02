from utils.models import Pet


class PetAPI:
    def __init__(self, client):
        self.client = client

    def get_pet_by_id(self, pet_id):
        url = f"/pet/{pet_id}"
        response = self.client.get(endpoint=url)
        if response.status_code == 200:
            Pet(**response.json())  # Validate response
        return response

    def get_pets_by_status(self, status):
        url = "/pet/findByStatus"
        params = {"status": status}
        response = self.client.get(endpoint=url, params=params)
        return response

    def add_pet(self, pet_data):
        pet = Pet(**pet_data)  # Validate input
        url = "/pet"
        response = self.client.post(endpoint=url, json=pet.model_dump())
        return response

    def update_pet(self, pet_data):
        pet = Pet(**pet_data)  # Validate input
        url = "/pet"
        response = self.client.put(endpoint=url, json=pet.model_dump())
        return response

    def delete_pet(self, pet_id):
        url = f"/pet/{pet_id}"
        response = self.client.delete(endpoint=url)
        return response

    def get_pets_by_tags(self, tags):
        url = "/pet/findByTags"
        params = {"tags": tags}
        response = self.client.get(endpoint=url, params=params)
        return response

    def update_pet_with_form(self, pet_id, name=None, status=None):
        url = f"/pet/{pet_id}"
        data = {}
        if name:
            data['name'] = name
        if status:
            data['status'] = status
        response = self.client.post(endpoint=url, data=data)
        return response

    def upload_image(self, pet_id, file_path, additional_metadata=None):
        url = f"/pet/{pet_id}/uploadImage"
        # Note: Requires HttpClient to support files
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {}
            if additional_metadata:
                data['additionalMetadata'] = additional_metadata
            response = self.client.post(endpoint=url, data=data, files=files)
        return response
