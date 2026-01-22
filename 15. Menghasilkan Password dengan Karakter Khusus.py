import secrets
import string

def generate_complex_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

password = generate_complex_password()
print(f"Password Kompleks: {password}")
# Fungsi: Membuat password yang kompleks dengan berbagai karakter.
# Kondisi: Ketika Anda ingin menyimpan password yang sangat aman.