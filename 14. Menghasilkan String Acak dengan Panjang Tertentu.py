import secrets
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

string_length = 16
random_string = generate_random_string(string_length)
print(f"String Acak dengan Panjang {string_length}: {random_string}")
# Fungsi: Menghasilkan string acak dengan panjang tertentu.
# Kondisi: Ketika Anda membutuhkan identifikasi akut yang dinamis.