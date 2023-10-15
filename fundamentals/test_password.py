from fundamentals.password import generate_password

def test_password_length():
    assert len(generate_password()) == 10

def test_password_alpha_characters():
    # generate password for testing purposes
    password = generate_password()

    assert password[0].isalpha()
    assert password[1].isalpha()
    assert password[2].isalpha()
    assert password[3].isalpha()
    assert password[4].isalpha()

def test_password_numberic_characters():
    # generate password for testing purposes
    password = generate_password()

    assert password[5].isdigit()
    assert password[6].isdigit()
    assert password[7].isdigit()
    assert password[8].isdigit()

def test_password_symbol_character():
    # generate password for testing purposes
    password = generate_password()

    assert contains(password[len(password) - 1], "!@#$%^&*")

def test_password_unique():
    # we ignore collisions for the purposes of this exercise
    password1 = generate_password()
    password2 = generate_password()

    assert password1 != password2

def contains(str, set):
    # check if any characters in set are present in str
    return 1 in [c in str for c in set]