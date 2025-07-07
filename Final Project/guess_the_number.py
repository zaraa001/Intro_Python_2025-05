import random

print("=== GAME TEBAK ANGKA ===")
print("Tebak angka dari 1 sampai 100!")
print("Kamu punya 10 kesempatan.")

angka_rahasia = random.randint(1, 100)
tebakan_pengguna = 0
jumlah_tebakan = 0
kesempatan_maksimal = 10
skor = 100

while jumlah_tebakan < kesempatan_maksimal:
    try:
        tebakan_pengguna = int(input("Tebakan kamu: "))
        jumlah_tebakan += 1

        if tebakan_pengguna < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan_pengguna > angka_rahasia:
            print("Terlalu besar!")
        else:
            print(f"Tebakanmu benar! Angkanya adalah {angka_rahasia}.")
            skor = max(0, 100 - (jumlah_tebakan - 1) * 10)
            print(f"Kamu menebak dalam {jumlah_tebakan} kali.")
            print(f"Skor akhir: {skor}")
            break

    except ValueError:
        print("Masukkan angka yang benar ya!")

if tebakan_pengguna != angka_rahasia:
    print(f"Kamu kehabisan kesempatan. Angka yang benar adalah {angka_rahasia}")
    print("Skor akhir: 0")
