# ==========================================================
# Latihan 4: Kombinasi Huruf
# Nama     : Aulia Rezki Rahman
# NIM      : J0403251009
# Kelas    : TPL A2
# ==========================================================
def kombinasi(n, hasil=""):
#fungsi di atas mendeklarasikan kombinasi dengan parameter n dan hasil. Dimana n merupakan panjang 
#karakter target dan hasil merupakan parameter kosong yang berfungsi untuk menyimpan nilai yang sedang dikerjakan
    if len(hasil) == n:
    #Kode di atas merupakan basecase yang memungkinkan fungsi rekrusi tidak melakukan perulangan
    #tanpa henti. Kondisi di atas mengisyaratkan jika fungsi len dengan parameter hasil sebanding dengan n,
        print(hasil)
        #maka print akan dijalankan dengan parameter hasil yang mengeluarkan output dari hasil yang ada sebelumnya.
        return
        #jika kondisi tidak memenuhi, return akan dieksekusi untuk berhenti dan mundur kembali ke kondisi sebelumnya,
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")
    #kode di atas merupakan kode rekrusif yang menciptakan percabangan, dimana nilai dari fungsi yang sudah ada
    #dimasukan dan akan ditambah dengan "A" atau "B" dalam penampungan hasil
kombinasi(2)
#kode di atas merupakan kode fungsi yang memasukan nilai ke dalam fungsi dengan nama yang 
# sama pada bagian sebelumnya dan meneksekusinya sesuai program yang dibuat 

#Dengan memanggil kombinasi(2), kita secara langsung menyuruh komputer untuk mulai membuat dan 
# menampilkan semua kemungkinan variasi huruf "A" dan "B" yang panjangnya tepat 2 karakter 
# yaitu AA, AB, BA, dan BB. Sama seperti contoh-contoh sebelumnya, tanpa baris pemanggilan ini, 
# program hanya akan diam mengingat aturan dan tidak akan menampilkan hasil apa pun di layar.
