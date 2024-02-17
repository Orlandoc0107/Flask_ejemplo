from werkzeug.security import check_password_hash, generate_password_hash

def codificar(password):
    resp = generate_password_hash(password)
    return resp


def descodificar(password, passwordDB):
    resp = check_password_hash(passwordDB, password)
    return resp
