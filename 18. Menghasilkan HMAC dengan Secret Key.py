import secrets
import hmac
import hashlib

def generate_hmac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

secret_key = secrets.token_bytes(16)
message = "Important Information"
hmac_value = generate_hmac(secret_key.decode(), message)
print(f"HMAC: {hmac_value}")
# Fungsi: Menghasilkan HMAC untuk informasi penting dengan kunci rahasia.
# Kondisi: Ketika Anda perlu mengamankan dan memverifikasi data penting.