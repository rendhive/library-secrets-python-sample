import secrets

def generate_secure_api_request_id():
    return secrets.token_hex(16)

api_request_id = generate_secure_api_request_id()
print(f"API Request ID: {api_request_id}")
# Fungsi: Menghasilkan ID permintaan API yang aman.
# Kondisi: Ketika Anda ingin melacak dan memastikan keamanan dalam setiap permintaan API.