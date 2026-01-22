import secrets
import string

def generate_secret_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

secret_code = generate_secret_code()
print(f"Kode Rahasia: {secret_code}")
# Fungsi: Membuat kode rahasia yang teracak menggunakan huruf dan angka.
# Kondisi: Ketika Anda ingin menghasilkan kode unik untuk autentikasi atau keperluan lain.