import secrets
import uuid

def generate_secure_uuid():
    return uuid.UUID(int=secrets.randbits(128))

secure_uuid = generate_secure_uuid()
print(f"UUID Aman: {secure_uuid}")
# Fungsi: Menghasilkan UUID yang aman menggunakan angka acak.
# Kondisi: Ketika Anda memerlukan identifikasi unik yang tidak mudah ditebak.