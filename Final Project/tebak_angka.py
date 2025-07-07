import random

class GameTebakAngka:
    def __init__(self):
        self.angka_rahasia = random.randint(1, 100)
        self.kesempatan = 10
        self.jumlah_tebakan = 0
        self.skor = 100

    def mulai(self):
        print("=== GAME TEBAK ANGKA (OOP) ===")
        print("Tebak angka dari 1 sampai 100!")
        print(f"Kamu punya {self.kesempatan} kesempatan.")

        while self.jumlah_tebakan < self.kesempatan:
            try:
                tebakan = int(input("Tebakan kamu: "))
                self.jumlah_tebakan += 1

                if tebakan < self.angka_rahasia:
                    print("Terlalu kecil!")
                elif tebakan > self.angka_rahasia:
                    print("Terlalu besar!")
                else:
                    print(f"Benar! Angkanya: {self.angka_rahasia}")
                    self.hitung_skor()
                    return
            except ValueError:
                print("Masukkan angka yang valid!")

        print(f"Sayang sekali! Angkanya adalah {self.angka_rahasia}")
        print("Skor akhir: 0")

    def hitung_skor(self):
        self.skor = max(0, 100 - (self.jumlah_tebakan - 1) * 10)
        print(f"Jumlah tebakan: {self.jumlah_tebakan}")
        print(f"Skor akhir: {self.skor}")

game = GameTebakAngka()
game.mulai()