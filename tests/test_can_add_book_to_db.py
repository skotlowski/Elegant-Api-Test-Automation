from pytest import mark


@mark.test
def test_can_add_book_to_db(session_logged, url):
    resource_url = f'{url}v1/resource'
    book_info_to_add = {
      "title": "The book 35",
      "authorFirst": "Name",
      "authorMiddle": "AuthorMiddleName",
      "authorLast": "AuthorLastName",
      "edition": "TheFirstEdition",
      "isbn10": "999966667777",
      "isbn13": "777799996666"
    }

    add_result = session_logged.post(
        url=resource_url,
        json=book_info_to_add
    )

    result_text = add_result.json()
    added_title = result_text.get('resource')
    title = added_title.get('title')
    expected_title = 'The book 35'

    assert title == expected_title
