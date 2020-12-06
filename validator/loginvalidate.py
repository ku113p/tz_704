import re

login_pattern = r'^[A-Za-z]$|^$|^[A-Za-z][A-Za-z\d\.\-]{0,18}[A-Za-z\d]$'

login_validation_functions = (
    lambda l: 0 <= len(l) <= 20,
    lambda l: l[0].isalpha() if l else True,
    lambda l: (l[-1].isdigit() or l[-1].isalpha()) if l else True,
    lambda l: all(map(
        lambda char: char.isalpha() or char.isdigit() or char in ('.', '-'),
        l[1:-1]
    )) if l else True
)


def is_login_valid_regex(login):
    return re.match(login_pattern, login) is not None


def is_login_valid_python_lambdas(login):
    return all(map(
        lambda f: f(login),
        login_validation_functions
    ))


def is_login_valid_python(login: str):
    if not login:
        return True

    if len(login) > 20:
        return False

    if not login[0].isalpha():
        return False

    if len(login) == 1:
        return True

    if not(login[-1].isalpha() or login[-1].isdigit()):
        return False

    for c in login[1:-1]:
        if not(c.isalpha() or c.isdigit() or c in ('-', '.')):
            return False

    return True
