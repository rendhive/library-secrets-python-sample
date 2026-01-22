import secrets

def generate_encryption_key():
    return secrets.token_bytes(16)  # Kunci 16 byte untuk AES

encryption_key = generate_encryption_key()
print(f"Kunci Enkripsi: {encryption_key.hex()}")
# Fungsi: Menghasilkan kunci untuk enkripsi simetris.
# Kondisi: Ketika Anda menggunakan algoritma enkripsi seperti AES.