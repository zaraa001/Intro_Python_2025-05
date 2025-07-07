import stok

def menu():
    data = stok.load_stok()

    while True:
        print("\n--- SISTEM STOK BARANG ---")
        print("1. List Stok")
        print("2. Tambah Barang")
        print("3. Simpan dan Keluar")

        pilih = input("Pilih menu (1-3): ")

        if pilih == "1":
            stok.tampilkan_stok(data)
        elif pilih == "2":
            nama = input("Nama barang: ")
            try:
                jumlah = int(input("Jumlah: "))
                stok.tambah_stok(data, nama, jumlah)
                print("Barang ditambahkan!")
            except ValueError:
                print("Jumlah harus angka!")
        elif pilih == "3":
            stok.simpan_stok(data)
            print("Data disimpan")
            break
        else:
            print("Menu tidak valid.")

menu()