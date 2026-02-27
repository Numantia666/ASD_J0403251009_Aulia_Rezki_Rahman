# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# Nama     : Aulia Rezki Rahman
# NIM      : J0403251009
# Kelas    : TPL A2
# ==========================================================
def cari_maks(data, index=0):
# kode di atas mendefinisikan fungsi cari_maks dengan dua parameter yaitu data dan index
#parameter data merupakan sesuatu yang dicari nilai terbesarnya sedangkan index merupakan
#posisi elemen yang sedang diperiksa
    if index == len(data) - 1:
        return data[index]
    #kondisi di atas merupakan base case yang memungkinkkan kode untuk berhenti. Jika kondisi index sebanding
    # dengan panjang dari data yang dikurang dengan satu, maka kode akan mengembalikan angka dengan 
    # parameter index

    maks_sisa = cari_maks(data, index + 1)
    #kode di atas ini merupakan kode rekrusif yang memungkinkan terjadinya perulangan. Kode terebut memasukan
    # nilai dari fungsi cari)maks yang parameter index nya di tambah 1 ke variabel maks_sisa
    if data[index] > maks_sisa:
        return data[index]
    #Kode di atas mengkondisikan jika data dengan parameter index lebih bedar dari maks_sisa,
    #maka program akan mengembalikan data dengan parameter index

    else:
        return maks_sisa
    #Jika kondisi sebelumnya tidak terpenuhi maka, else akan dijalankan dengan mengembalikan maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))
#Bagian kode ini adalah langkah penutup untuk menggunakan fungsi yang sudah kita 
# buat sebelumnya. Pertama, kita menyiapkan sebuah daftar berisi lima angka dan 
# menyimpannya ke dalam wadah variabel bernama angka. Setelah itu, perintah print 
# bertugas memanggil fungsi cari_maks untuk mencari angka paling besar dari daftar 
# tersebut, lalu langsung menampilkan hasilnya ke layar dengan awalan teks "Nilai maksimum:".
