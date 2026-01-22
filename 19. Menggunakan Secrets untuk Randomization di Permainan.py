import secrets

def random_choice(choices):
    return secrets.choice(choices)

options = ["rock", "paper", "scissors"]
random_option = random_choice(options)
print(f"Pilihan Acak: {random_option}")
# Fungsi: Membuat pilihan acak dari opsi yang diberikan.
# Kondisi: Ketika Anda ingin memberikan elemen ketidakpastian, seperti dalam permainan.