import secrets

def generate_unique_id():
    return secrets.token_urlsafe(16)

unique_id = generate_unique_id()
print(f"ID Unik: {unique_id}")
# Fungsi: Menghasilkan ID yang unik dan aman.
# Kondisi: Ketika Anda perlu mengidentifikasi entitas secara unik dalam aplikasi.