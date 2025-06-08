#int: bil bulat (0,1,2,3,...)

x = 36789 #batas max yg diambil, kalo  mau ambil yang triliun || kuadriliun tambahin simbol, ex: x = 36789 + 'T'
print("Ini contoh data int : {0}".format(x))  

#float
y = 1.788
print("Ini contoh data float : {0}".format(y))  

#compleks
z = 2 + 7j
print("Ini contoh data compl : {0}".format(z))  

#sequence 
a = [1,2,3] #list, sifat data type nya sama (sebisa mungkin)
print("Ini contoh data list : {0}".format(a))
b = (4,5,6) #truplet, sifat data type nya ga bisa di ganti
print("Ini contoh data truplet : {0}".format(b))  
#range
c = range (1,9)
print("Ini contoh data range : {0}".format(c))  

#non-primitive
#text
nama = "Zara" #data type str "" max 255 char, char ''
print("Ini contoh data nama : {0}".format(nama))  
#karakter
karakter = 'T'
print("Ini contoh data karakter : {0}".format(karakter))  

#final data type/set
f = {1,3,2} #tipe data yang ga bisa di ganti
print("Ini contoh data set : {0}".format(f))  
#frozenset
g = ({6,7,8})
print("Ini contoh data frozenset : {0}".format(g))  

#cond data type
#bool: True(1), False(0)
kondisi_badan = True

#binery
i = 0b1000001
print("tipe data binary : {0}".format(i))  
#desimal = int(i)
#print("cnv binary to desimal : {0}".format(desimal))  
#char = chr(desimal)
#print("cnv binary to desimal : {0}".format(char)) 
print("singkat binary to char : {0}".format(chr(int(i))))  

#binary array
j = bytearray(a)
print("isi binary dlm var a : {0}".format(j))  
z = memoryview(j)
print("lokasi array dalam memory : {0}".format(z))