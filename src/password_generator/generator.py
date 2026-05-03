import secrets
import string


def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special=True):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Pelo menos um critério deve ser selecionado.")

    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password