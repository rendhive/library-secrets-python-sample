import secrets

def generate_web_token():
    return secrets.token_hex(16)  # Menghasilkan token web yang aman

web_token = generate_web_token()
print(f"Token Web: {web_token}")
# Fungsi: Menghasilkan token untuk otentikasi aplikasi web.
# Kondisi: Ketika Anda butuh sistem manajerial session atau token untuk aplikasi.