# ==========================================================
# Studi Kasus: Generator PIN
# Nama     : Aulia Rezki Rahman
# NIM      : J0403251009
# Kelas    : TPL A2
# ==========================================================
def buat_pin(panjang, hasil=""):
# fungsi di atas mendeklarasikan buat_pin dengan parameter panjang dan hasil. Parameter panjang merupakan 
# parameter utama yang menjadi batas dari pin yang akan dibuat. Sedangkan hasil merupakan parameter
#opsional yang berfungsi untuk menyimpan data ketika sedang mengeksekusi program dan nilainya akan berubah
#pada setiap langkah
    if len(hasil) == panjang:
    #fungsi base case di atas mengkondisikan ketika panjang dari parameter hasil sebanding dengan parameter panjang,
    
        print("PIN:", hasil)
        #maka kode print akan diekseskusi
        return
        #kode di atas membuat kode kembali ke cabang sebelumnya sehingga memungkinkan terjadinya perulangan
    for angka in ["0", "1", "2"]:
    #kode di atas merupakan kode rekrusif yang diperkuat dengan loop. program for akan mencabangkan teks yang ada
    #saat ini dengan huruf yang ada pada kurung.
        buat_pin(panjang, hasil + angka)

buat_pin(3)
#kode di atas memasukan nilai parameter menjadi 3, maka akan ada kombinasi 3 pangkat 3
# atau akan ada sebanyak 27 kombinasi PIN

# Di sini, kita memerintahkan komputer untuk mencetak semua kemungkinan PIN yang panjangnya 3 
# digit karena ada angka 3 di dalam kurung. Tanpa baris pemanggilan ini, kode sebelumnya 
# hanya akan diam menunggu dan tidak menghasilkan apa-apa.
