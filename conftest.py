from pytest import fixture
from requests import Session
from selenium import webdriver


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
def headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }


@fixture
def session_logged(email, password, headers):
    session = Session()

    # Mimic common User-Agent
    session.headers.update(headers)
    
    # Mimic navigating to the lading page
    session.get(url='http://127.0.0.1:5000/')

    # Login with a POST
    login_info = {
        'email': email,
        'password': password
    }

    session.post(url='http://127.0.0.1:5000/v1/login', data=login_info)

    return session


@fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
