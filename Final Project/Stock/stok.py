import csv

def load_stok(filename="stok.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            return {rows[0]: int(rows[1]) for rows in reader}
    except FileNotFoundError:
        return {}

def simpan_stok(stok, filename="stok.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        for barang, jumlah in stok.items():
            writer.writerow([barang, jumlah])

def tampilkan_stok(stok):
    if not stok:
        print("Belum ada data stok.")
    else:
        print("\nStok Barang:")
        for barang, jumlah in stok.items():
            print(f"{barang}: {jumlah} pcs")

def tambah_stok(stok, nama_barang, jumlah):
    if nama_barang in stok:
        stok[nama_barang] += jumlah
    else:
        stok[nama_barang] = jumlah