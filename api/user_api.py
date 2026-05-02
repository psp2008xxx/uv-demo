from utils.models import User


class UserAPI:
    def __init__(self, client):
        self.client = client

    def create_user(self, user_data):
        user = User(**user_data)  # Validate input
        url = "/user"
        response = self.client.post(endpoint=url, json=user.model_dump())
        return response

    def create_users_with_list(self, users_list):
        # Validate each user
        for user_data in users_list:
            User(**user_data)
        url = "/user/createWithList"
        response = self.client.post(endpoint=url, json=users_list)
        return response

    def create_users_with_array(self, users_list):
        # Validate each user
        for user_data in users_list:
            User(**user_data)
        url = "/user/createWithArray"
        response = self.client.post(endpoint=url, json=users_list)
        return response

    def login_user(self, username, password):
        url = "/user/login"
        params = {"username": username, "password": password}
        response = self.client.get(endpoint=url, params=params)
        return response

    def logout_user(self):
        url = "/user/logout"
        response = self.client.get(endpoint=url)
        return response

    def get_user_by_username(self, username):
        url = f"/user/{username}"
        response = self.client.get(endpoint=url)
        if response.status_code == 200:
            User(**response.json())  # Validate response
        return response

    def update_user(self, username, user_data):
        user = User(**user_data)  # Validate input
        url = f"/user/{username}"
        response = self.client.put(endpoint=url, json=user.model_dump())
        return response

    def delete_user(self, username):
        url = f"/user/{username}"
        response = self.client.delete(endpoint=url)
        return response
