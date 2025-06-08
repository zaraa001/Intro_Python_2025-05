# inisialisasi, teknik program menyediakan memo yg akan di pakai
#list tipe datanya nya harus sama, ga bisa disisip jadi harus terurut

makanan = ["donat","ikan","mochi"]

# read (R)
print(f"List Makanan : {makanan}")

# read spesifik
print(f"Index of -1 : {makanan[-1]}") 
print(f"Index of 0 : {makanan[0]}")
print(f"Index of -3 : {makanan[-3]}")

# upd (U)
makanan[2] = "ayam"
print(f"List Makanan setelah di upd : {makanan}")

#nambahin data append (a)
makanan.append("mochi")
print(f"List Makanan setelah append : {makanan}")

# Delete (remove)
makanan.remove("ayam")
print(f"List Makanan setelah delete : {makanan}")

buah = ["apel","pir","salak"]
makanan += buah
print(f"List Makanan setelah add list : {makanan}")

