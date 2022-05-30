from requests import Session
from pytest import mark


@mark.test
def test_can_login_using_api_request(email, password):
    session = Session()

    # Mimic navigating to the lading page
    landing_page_resp = session.get(url='http://127.0.0.1:5000/')

    #print(landing_page_resp.text)
    #print(f'Cookies: {session.cookies}')
    #print(f'Headers: {session.headers}')

    # Login with a POST
    login_info = {
        'email': email,
        'password': password
    }

    login_resp = session.post(url='http://127.0.0.1:5000/v1/login', data=login_info)

    assert login_resp.status_code == 200
