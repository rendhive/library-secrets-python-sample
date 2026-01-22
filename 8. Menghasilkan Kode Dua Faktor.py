import secrets

def generate_otp():
    return secrets.randbelow(10**6)  # Menghasilkan OTP 6 digit

otp = generate_otp()
print(f"Kode OTP: {otp:06d}")
# Fungsi: Menghasilkan kode OTP (One Time Password) yang aman.
# Kondisi: Ketika Anda butuh verifikasi dua faktor dalam logika autentikasi.