import secrets

def generate_random_number():
    return secrets.randbelow(100)  # Menghasilkan angka acak dari 0 hingga 99

random_number = generate_random_number()
print(f"Angka acak: {random_number}")
# Fungsi: Menghasilkan angka acak dalam rentang tertentu.
# Kondisi: Ketika Anda memerlukan angka acak untuk keperluan seperti penomoran atau pemilihan acak.