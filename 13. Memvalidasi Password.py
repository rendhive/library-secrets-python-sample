import secrets
import hashlib

def secure_password_hash(password):
    salt = secrets.token_bytes(16)  # Membuat salt secara acak
    return salt + hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def validate_password(stored_password, provided_password):
    salt = stored_password[:16]  # Ambil salt dari password yang disimpan
    hashed_provided = salt + hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    return secrets.compare_digest(stored_password, hashed_provided)

password = "my_secure_password"
stored_password = secure_password_hash(password)

is_valid = validate_password(stored_password, "my_secure_password")
print(f"Password valid: {is_valid}")
# Fungsi: Mengelola pengamanan password dengan hashing dan salt.
# Kondisi: Ketika menyimpan dan memvalidasi password pengguna secara aman.