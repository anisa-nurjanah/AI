def jumlah(a,b):
    return a+b**2
    print(jumlah(5,4))

def jumlah1(a,b):
    return a+b
def jumlah2(a,b):
    print(a+b)
    return a+b

# a = jumlah1(2,3)
# print("a:",a)
b = jumlah2(2,3)
print("b :",b)

#cara ngeprint ada 3: pake koma(,), 
					#(%) contohnya dibawah lebih spesifik soal type datanya, misal print("ab:%d %f"%(a,b))
					#{}, misal print("a :{}".format(a,b)) biasanya buat ngeprint yg variabelnya banyak


def biodata(nama,prodi,status="Mahasiswa S1"):
	print("Nama :%s"%nama.capitalize())
	print("Prodi :%s"%prodi.capitalize())
	print("Status :%s"%status.capitalize())
	print()
	
biodata("budi","ilmu komputer",) #bakal ngeprint nama : budi, prodi : ilkom, status : mahasiswa s1 karna udh di set sblmnya
biodata("budi","ilmu komputer","Alumni")
	
	
#argumen
def function(a,b,c):
	return a+b+c
	
print(function(1,b=2,c=3))
#print(function(a=1,2,3)) >>> bakal error
#syarat : depan gaboleh pake a=..., kalo pake a=... blakangnya harus ikutin pake sama dengan.
#dan bisa dituker misal print(function(b=2,a=3,c=5))


#variabel length argument
def nilai(nama,prodi,*skor):
	print("Nama :%s"%nama.capitalize())
	print("Prodi :%s"%prodi.capitalize())
	print("Skor :",skor)
	for i in range(len(skor)):
		print("Skor ke-%d = %.f"%(i,skor[i]))

nilai("budi","ilmu komputer",90,80,70,50)
#outp sama kek biodata, tp nilai ke 1 : 90, nilai ke-2 : 80, nilai ke-3 : 70 dll.
#nilai("budi","ilmu komputer",90,80,"selesai"), outputnya nilai ke 1 : 90, nilai ke-2 : 80, nilai ke-3 :selesai

#keyword length argument
def total(*banyak,**keywords):
	print("banyak :", banyak, type(banyak))
	print("keywords :",keywords,type(keywords))
	#for i in range (len(banyak)):
	#	print("Jumlah ke-%d : %.f"%(i,banyak[i]))
		
	for i in keywords.items():
		print("Keywords %s : %d" %(i[0],i[1]))
total(1,2,3,4,a=1,b=2,c=3)

#kalo mau keynya dan valuenya apa aja 
keywords = {
	"a" : 1,
	"b" : 2
}
#keys nya a, valuesnya 1
keywords.keys()
keywords.values()

list(keywords.keys())[0]
list(keywords.values())[0]

print("keys :")
for i in keywords.items():
	print(i[0])
print("values :")
for i in keywords.values():
	print(i[1])


#perbedaan
#lists = [1,2,3,4]	# isinya bisa diubah
#tuples = (1,2,3,4)	# isinya gabisa diubah
#dictionary = {		# akses pake string
	#"satu" :1,
	#"dua" :2
	#}

#kepemilikan variabel
x=50 #var global
def fungsi(i):
	x = i**2 #var lokal
	print("x di variabel lokal: ", x) #output 25 knp? karena dapet dari angka 5 di fungsi(5)
fungsi (5)
print("x di variabel global :", x)

#higher order function
def kuadrat(x): ##baru masuk fungsi ini
	print("masuk ke fungsi kuadrat")
	return x**2 
def apply(i,j):
	print("masuk ke fungsi apply")
	return i(j) #return kuadrat 2 #awalnya masuk sini dulu kuadrat(sbg i),2(sbg j) nya jadi fungsi
print(apply(kuadrat,2))


#class
class PersegiPanjang :
	def __init__(self, panjang, lebar):
		self.panjang=panjang
		self.lebar=lebar
	def hitung_luas(self):
		return self.panjang*self.lebar
	def hitung_keliling(self):
		return (2*self.panjang)+(2*self.lebar)
	def gambar_persegi_panjang(self):
		for i in range (0,self.lebar):
			for j in range(0, self.panjang):
				print('*',end="")
			print()
			
PersegiPanjangA = PersegiPanjang(20,10) #20 sbg panjang, 1- sbg lebar
print ("Panjang persegi panjang A :", PersegiPanjangA.panjang)
print ("Panjang persegi lebar A :", PersegiPanjangA.lebar)
print ("Luas persegi panjang A :", PersegiPanjangA.hitung_luas())
print ("Keliling persegi panjang A :", PersegiPanjangA.hitung_keliling())
print ("Menggambar persegi panjang A :") #ga minta di return karna masuknya pasti ke anu jadi ga sama kek lainnya


