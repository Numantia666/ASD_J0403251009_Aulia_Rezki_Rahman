# ==========================================================
# Latihan 2: Tracing Rekursi
# Nama     : Aulia Rezki Rahman
# NIM      : J0403251009
# Kelas    : TPL A2
# ==========================================================
def countdown(n):
#kode di atas mendefenisikan fungsi countdown dengan parameter n
    if n == 0:
        print("Selesai")
        return
    # Kode di atas merupakan base case yang membuat fungsi rekrusif berhenti. Dengan mengkondisikan
    # parameter n dengan 0, maka program akan menampilkan pesan "Selesai" dan 
    # return akan mengembalikan kode ke langkah awal sebelumnya
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)
    # Ketiga kode di atas merupakan kode inti. Di mana kode baris pertama sebelum memasuki
    # rekrusi akan menampilkan output "Masuk" dan parameter n
    # kode pada baris pertama akan mengurangi nilai dari parameter n dengan 1
    # kode pada baris ke tiga akan mengeluarkan output "Keluar" dan para meter n
countdown(3)
# Saat countdown(3) dipanggil, program mulai menyelam dengan mencetak "Masuk" secara berurutan 
# menurun (3, 2, 1) dan menunda sementara eksekusi baris pencetakan "Keluar" ke dalam memori komputer.
# Begitu nilai mencapai 0, program mencetak "Selesai" sebagai tanda dasar rekursi tercapai, 
# lalu mulai berjalan mundur untuk mengeksekusi sisa baris yang tertunda tadi dari tumpukan paling atas, 
# sehingga mencetak "Keluar" secara berurutan naik (1, 2, 3) hingga prosesnya benar-benar selesai di 
# titik awal pemanggilan.
