import datetime

nama_pt = "PT.Bintang Jaya"
alamat = "Jl. abc 70 No 1, Jakbar"
waktu_dibuat = datetime.datetime.now()

# posisional argumen
print ("=======Posisional Argumen=======")
print ("\t\t\t{0}\nKepada,\nHRD Manager {1}\n{2}".format(nama_pt,alamat,waktu_dibuat))
print ("=======Keyword Argumen=======")
print ("\t\t\t{waktu}\nKepada,\nHRD Manager {nama_pt}\n{alamat}".format(nama_pt = nama_pt,alamat = alamat,waktu= waktu_dibuat))
print ("=======Cara Singkat=======")
print (f"\t\t\t{waktu_dibuat}\nKepada,\nHRD Manager {nama_pt}\n{alamat}")
# t itu tab 4x spasi, n itu new line