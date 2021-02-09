from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "victoraugusto6", "id": 48570599,
        "avatar_url": "https://avatars.githubusercontent.com/u/48570599?v=4"}
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('victoraugusto6')
    assert 'https://avatars.githubusercontent.com/u/48570599?v=4' == url
