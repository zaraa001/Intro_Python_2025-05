# cara nulis dgn singkat

employe = [
    {
        "nama" : "Zara",
        "pekerjaan" : "IT",
        "gaji" : 800
    },
    { 
        "nama" : "Za",
        "pekerjaan" : "IT"
    },
    {
        "nama" : "Zra",
        "pekerjaan" : "IT"
    }
]

# funct void
def detail_pekerja(nama,pekerjaan,gaji = None):
    print(f"Nama : {nama}")
    print(f"Pekerjaan : {pekerjaan}")
    print(f"Gaji : {gaji}")
    print(f"Pekerja yang rajin")

# cara panggil
detail_pekerja(employe[0]['nama'],employe[0]['pekerjaan'],employe[0]['gaji'])
detail_pekerja(employe[1]['nama'],employe[1]['pekerjaan'])
detail_pekerja(employe[2]['nama'],employe[2]['pekerjaan'])

def penjumlahan(a,b):
    return a + b

hasil_penjumlahann = penjumlahan(11,12)
print(f"Hasil dari penjumlahan : {hasil_penjumlahann}")