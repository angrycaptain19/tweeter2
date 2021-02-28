from flask_bcrypt import check_password_hash, generate_password_hash

def generate_hash(password):
    return generate_password_hash(password)

def check_hash(password_claim, stored_hash):
    return check_password_hash(password_claim, stored_hash)