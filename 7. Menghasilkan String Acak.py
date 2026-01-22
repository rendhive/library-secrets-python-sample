import secrets
import string

def generate_random_string(length=10):
    characters = string.ascii_letters
    return ''.join(secrets.choice(characters) for _ in range(length))

random_string = generate_random_string()
print(f"String Acak: {random_string}")
# Fungsi: Membuat string acak menggunakan huruf saja.
# Kondisi: Ketika Anda perlu membuat deteksi input atau nama acak.