import secrets

def generate_secret_key():
    return secrets.token_bytes(32)  # Menghasilkan kunci rahasia 32 byte

secret_key = generate_secret_key()
print(f"Kunci Rahasia: {secret_key.hex()}")
# Fungsi: Menghasilkan kunci rahasia yang aman bagi kriptografi.
# Kondisi: Ketika Anda membutuhkan kunci untuk operasi enkripsi.