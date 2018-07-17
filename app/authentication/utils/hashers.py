import six
from app import BCRYPT


def make_password(raw_password):
    """
    simple function to generate password hashes
    :param raw_password:
    :return: hashed_password
    """
    
    hashed_password = BCRYPT.generate_password_hash(raw_password)
    if six.PY2:
        return hashed_password
    else:
        return hashed_password.decode('utf-8')
