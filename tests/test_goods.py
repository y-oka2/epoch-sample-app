import pytest
from api_app.goods import app


def test_goods_currencies():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/currencies')
    body = result.get_json()

    assert 200 == result.status_code
    assert 'currencies' in body
    assert 0 < len(body['currencies'])

