from pytest import mark


@mark.test
def test_search(session_logged, url):
    url = f'{url}v1/search?title='
    expected_title = 'The book 35'
    search_result = session_logged.get(url=f'{url}{expected_title}')
    res = search_result.json().get('results')
    res_list = res[0]
    title = res_list.get('title')

    assert title == expected_title
