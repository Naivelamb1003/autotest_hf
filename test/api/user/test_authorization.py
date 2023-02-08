import pytest
import requests
from json import dumps

from modules.api.clients.user_clients import UserClient
from test.api.user.data.auth import UserEnum

client = UserClient()


@pytest.mark.http
def test_existing_user_should_return_success():
    response = client.auth(dumps(UserEnum.VALID_USER_TUPLE))
    assert response.status_code == requests.codes.ok
    assert response.as_dict["token"] != ""


@pytest.mark.http
def test_incorrect_email_should_return_code_error():
    response = client.auth(dumps(UserEnum.INVALID_EMAIL_TUPLE))
    assert response.status_code == requests.codes.not_found  # got 404 on wrong email, not presented in docs


@pytest.mark.http
def test_incorrect_password_should_return_code_error():
    response = client.auth(UserEnum.INVALID_PASS_TUPLE)
    assert response.status_code == requests.codes.bad
