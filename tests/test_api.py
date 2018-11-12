import pytest


@pytest.mark.last
def test_req_log(client):
    resp = client.get('/req-log/')

    assert resp.status_code == 200
    assert type(resp.get_json().get('data')) is list


@pytest.mark.last
def test_resp_log(client):
    resp = client.get('/resp-log/')

    assert resp.status_code == 200
    assert type(resp.get_json().get('data')) is list


@pytest.mark.last
def test_logs(client):
    resp = client.get('/logs/')

    assert resp.status_code == 200
    assert type(resp.get_json().get('data')) is list
