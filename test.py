from blahblah import fake
from district42 import json_schema as schema

from api import API
from helper import decode_token


def test_authenticate_created_account():
    # there is a user device
    device_id = fake(schema.string.non_empty)

    # with this device user creates an account and receives token
    create_account_response = API().create_account(
        device_id=device_id
    )
    assert create_account_response.status_code == 200
    created_account = create_account_response.json()

    created_account_token = created_account['token']

    # with received token user authenticates an account
    authenticate_account_response = API(created_account_token).authenticaticate_account(
        username=fake(schema.string.non_empty),
        password=fake(schema.string.non_empty),
        device_id=device_id
    )
    assert authenticate_account_response.status_code == 200
    authenticated_account = authenticate_account_response.json()

    decoded_auth_token = decode_token(authenticated_account['token'])

    # profileId from a decoded authentication token matches profileId from a created account
    assert decoded_auth_token['profileId'] == created_account['profileId']
    # and an account state is not automatically approved
    assert decoded_auth_token['accountState'] == 'pending_approval'
