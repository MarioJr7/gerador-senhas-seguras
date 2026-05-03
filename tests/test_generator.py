import string
from password_generator.generator import generate_password

def test_password_length():
    password = generate_password(length=20)
    assert len(password) == 20


def test_password_uppercase():
    password = generate_password(
        uppercase=True,
        lowercase=False,
        numbers=False,
        special=False
    )
    assert any(char in string.ascii_uppercase for char in password)


def test_password_numbers():
    password = generate_password(
        uppercase=False,
        lowercase=False,
        numbers=True,
        special=False
    )
    assert any(char in string.digits for char in password)


def test_invalid_criteria():
    try:
        generate_password(
            uppercase=False,
            lowercase=False,
            numbers=False,
            special=False
        )
        assert False
    except ValueError:
        assert True