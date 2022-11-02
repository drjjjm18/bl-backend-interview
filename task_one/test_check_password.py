import pytest

from check_password import check_password


@pytest.mark.parametrize("password,expected",
                         [
                             ('z', 6),
                             ('aA1', 4),
                             ('1377C0d3', 0),
                             ('qqqwertyuiopasdfghjklzxcv', 2),
                             ('qqqwertyuiopasdfghjklzxcvbnm', 4),
                             ('123456', 2)
                            ])
def test_checkpassword(password, expected):
    output = check_password(password)
    assert expected == output


def test_checkpassword_type_error():
    with pytest.raises(TypeError):
        output = check_password(['bad', 'type'])
