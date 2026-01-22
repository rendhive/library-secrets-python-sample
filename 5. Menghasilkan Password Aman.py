import secrets
import string

def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

secure_password = generate_secure_password()
print(f"Password Aman: {secure_password}")
# Fungsi: Membuat password yang kuat dengan kombinasi huruf, angka, dan simbol.
# Kondisi: Ketika Anda memerlukan password yang aman untuk keperluan login.