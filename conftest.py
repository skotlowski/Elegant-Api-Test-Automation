from pytest import fixture
from requests import Session


@fixture
def email():
    return 'toushirouu@gmail.com'


@fixture
def password():
    return '1234'


@fixture
def url():
    return 'http://127.0.0.1:5000/'


@fixture
def session_logged(email, password):
    session = Session()

    # Mimic navigating to the lading page
    landing_page_resp = session.get(url='http://127.0.0.1:5000/')

    # Login with a POST
    login_info = {
        'email': email,
        'password': password
    }

    login_resp = session.post(url='http://127.0.0.1:5000/v1/login', data=login_info)

    return session
