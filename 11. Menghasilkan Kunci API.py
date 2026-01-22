import secrets

def generate_api_key():
    return secrets.token_urlsafe(32)  # Menghasilkan kunci API yang aman dan URL friendly

api_key = generate_api_key()
print(f"Kunci API: {api_key}")
# Fungsi: Menghasilkan kunci API yang aman dan dapat digunakan dalam URL.
# Kondisi: Ketika Anda membangun API dan butuh kunci untuk akses pengguna.