from pytest import mark


@mark.test
def test_login_with_request_and_browser(session_logged, browser, url):
    token = session_logged.cookies.get('token')
    browser.get(url)
    browser.add_cookie(
        {
            'name': 'token',
            'value': token
        }
    )
    browser.get(f'{url}search')
    expected_content = 'Search for a book!'
    assert expected_content in browser.page_source
