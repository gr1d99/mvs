"""
    Provide helper functions to ease authentication process
    of authenticating users
"""

from flask import url_for


def login_user(client, email: str, password: str):
    """
    makes request to authenticate user
    :param client: test client
    :param email: user email
    :param password: user password
    :return: response object
    """

    response = client.post(
        url_for('authentication_app.login'),
        data=dict(
            email=email,
            password=password
        )
    )

    return response


def user_token(response):
    """
    gets user auth_token from response object
    :param response: object
    :return: string
    """

    return response.json['auth_token']


def logout_user(client, token: str):
    """
    makes request to logout user
    :param token: test client
    :return: response object
    """

    response = client.delete(
        url_for('authentication_app.logout'),
        headers={'Authorization': 'Bearer {}'.format(token)}
    )

    return response
