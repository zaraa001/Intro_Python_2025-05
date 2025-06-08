# study case
#di pake saat ragu
# pake switch case dan ada di python 3 (kalo comp nya bisa)

nilai_rapot = 100

# if, format nya:
#  if kondisi :
#   apa yang akan dilakukan jika kondisi terpenuhi
# kalau tidak terpenuhi program akan tetap jalan

print ("========IF=========")
nilai_rapot = 70
if nilai_rapot >= 100:
    print("Selamat kamu lulus")
print("Program bakal lanjut")

print ("========IF=========")
nilai_rapot = 100
if nilai_rapot >= 100:
    print("Selamat kamu lulus")
print("Program bakal lanjut")

# bakal maksa terus 
print ("========IF ELSE =========")
nilai_rapot = 60
if nilai_rapot >= 100:
    print("Selamat kamu lulus")
else :  
    print("Silahkan coba lagi")

print ("========IF ELSE =========")
nilai_rapot = 100
if nilai_rapot >= 100:
    print("Selamat kamu lulus")
else :  
    print("Silahkan coba lagi")

# liat sikon mau pake yang mana, tergantung ke kompleks-an nya
print ("========Tenery=========")
nilai_rapot = 60
pesan = "Lulus" if nilai_rapot >= 100 else "Tidak Lulus"
print(f"{pesan}")

print ("========IF ELIF ELSE=========")
nilai_rapot = 60
if nilai_rapot >= 100:
    print("Selamat kamu lulus")
elif nilai_rapot >= 50 and nilai_rapot<100:  
    print("Lulus dengan nilai pas-pasan")
else:
    print("Coba Lagi")

# nested if
print ("========NESTED IF=========")
nilai_rapot = 60
if nilai_rapot >= 100: #kondisi 1
    print("Selamat kamu lulus")
elif nilai_rapot >= 50 and nilai_rapot<100: #kondisi 2
    if nilai_rapot > 70: #disebut nested if
        print("Lulus")
    else:
        print("Lulus dengan nilai pas-pasan")
else: #pilihan kalau 1&2 ga bisa
    print("Coba Lagi")

#cara profesional "cari syarat yang paling sedikit/cari salah nya"

# switch case (dipakai saat tau spesifik apa yg user pilih)
print ("Switch Case=========")
print ("=========Menu")
print ("1. Start")
print ("2. End")
select = input("Select>= ")
match select:
    case "1":
        print("Start")
    case "2":
        print("End")
    case _:
        print("Invalid Input Type")


