import secrets

def generate_salt():
    return secrets.token_bytes(16)  # Salt 16 byte

salt = generate_salt()
print(f"Salt: {salt.hex()}")
# Fungsi: Menghasilkan salt yang digunakan dalam hashing.
# Kondisi: Ketika Anda memerlukan pengacakan yang aman untuk hashing.