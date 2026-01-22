import secrets

def generate_token():
    return secrets.token_hex(16)

token = generate_token()
print(f"Token Otentikasi: {token}")
# Fungsi: Menghasilkan token otentikasi yang aman, dalam format heksadesimal.
# Kondisi: Ketika Anda perlu membuat token yang sulit ditebak untuk autentikasi.