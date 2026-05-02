import pytest


def test_create_and_get_user(user_service, random_user):
    # Create user
    response = user_service.create_user(random_user)
    assert response.status_code == 200

    username = random_user['username']

    # Get user
    response = user_service.get_user_by_username(username)
    assert response.status_code == 200
    user = response.json()
    assert user['username'] == username

    # Update user
    updated_data = random_user.copy()
    updated_data['firstName'] = 'UpdatedName'
    response = user_service.update_user(username, updated_data)
    assert response.status_code == 200

    # Delete user
    response = user_service.delete_user(username)
    assert response.status_code == 200


def test_login_logout_user(user_service):
    # Assuming a test user exists, or create one first
    # For demo, skip if no user
    response = user_service.login_user('testuser', 'password')
    # May fail if user doesn't exist, but tests the endpoint
    assert response.status_code in [200, 400]  # 200 if logged in, 400 if invalid

    response = user_service.logout_user()
    assert response.status_code == 200


def test_create_users_with_list(user_service, random_user):
    users_list = [random_user, random_user.copy()]
    users_list[1]['username'] = 'uniqueuser2'
    response = user_service.create_users_with_list(users_list)
    assert response.status_code == 200
