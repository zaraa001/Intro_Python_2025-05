#read
profile = {
    "nama" : "Zara",
    "jurusan" : ["IT","IS"],
    "umur" : 19,
    "ketua_kelas" : "Yusuf"
}
print(f"Dict Data : {profile}")
print(f"Nama : {profile['nama']}")
print(f"Jurusan : {profile["jurusan"][0]}") #cara ambil yg jurusan it doang
print(f"Umur : {profile['umur']}")

#upd
profile ['umur'] = 20
print(f"Dictionary Data : {profile}")
profile ['ketua kelas'] = "Ahmad"
print(f"Dictionary Data : {profile}")

#del
del profile ['ketua_kelas']
print(f"Dictionary Data : {profile}")