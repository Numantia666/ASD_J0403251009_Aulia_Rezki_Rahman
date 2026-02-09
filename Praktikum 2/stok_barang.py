# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama :Aulia Rezki Rahman
# NIM :J0403251009
# Kelas : TPL A2
# ==========================================================
# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(NAMA_FILE):
    stok_dict = {} # Inisialisasi data dictionary

    with open(NAMA_FILE,"r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            KodeBarang, NamaBarang, Stok = baris.split(',')
            stok_dict[KodeBarang] = {"NamaBarang" : NamaBarang, "Stok" : Stok}
    return stok_dict
    
Buka_Data = baca_stok(NAMA_FILE)
print("Jumlah data adalah", len(Buka_Data))

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(NAMA_FILE, stok_dict):
    with open(NAMA_FILE, "w", encoding="utf=8") as file:
        for KodeBarang in sorted(stok_dict.keys()):
            NAMA_FILE = stok_dict[KodeBarang]["NamaBarang"]
            Stok = stok_dict[KodeBarang]['Stok']
            file.write(f'{KodeBarang},{NAMA_FILE},{Stok}\n')

simpan_stok(NAMA_FILE, Buka_Data)
print("\nData Berhasil Disimpan", NAMA_FILE) 





# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    print("\n=== Daftar Barang")
    print(f"{'KodeBarang' :<10} | {'NamaBarang' :<12} | {'Stok' :>5}")
    print("="*32)

    for KodeBarang in sorted(stok_dict.keys()):
        NamaBarang = stok_dict[KodeBarang]['NamaBarang']
        Stok = stok_dict[KodeBarang]['Stok']
        print(f'{KodeBarang:<10} | {NamaBarang:<12}| {int(Stok):>5}')

print(tampilkan_semua(Buka_Data))



# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    kode = input("Masukan kode barang: ").strip()

    if kode in stok_dict:
        NamaBarang = stok_dict[kode]["NamaBarang"]
        Stok = stok_dict[kode]["Stok"]

        print(f'KodeBarang :{kode}')
        print(f'NamaBarang :{NamaBarang}')
        print(f'Stok :{Stok}')

    else:
        print("Barang Tidak Ditemukan")




# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()
        
    if kode in stok_dict:
        print("Error: Kode sudah digunakan!")
        return

    nama = input("Masukkan nama barang: ").strip()
        
    try:
        stok_awal = int(input("Masukkan stok awal: "))
        stok_dict[kode] = {"NamaBarang": nama, "Stok": str(stok_awal)}
        print(f"Barang '{nama}' berhasil ditambahkan ke sistem.")
    except ValueError:
        print("Error: Stok harus berupa angka!")



# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan. Update dibatalkan.")
        return

    print(f"Barang: {stok_dict[kode]['NamaBarang']} (Stok saat ini: {stok_dict[kode]['Stok']})")
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
        stok_sekarang = int(stok_dict[kode]['Stok'])

        if pilihan == "1":
            stok_baru = stok_sekarang + jumlah
            stok_dict[kode]['Stok'] = str(stok_baru)
            print("Update berhasil: Stok bertambah.")
        elif pilihan == "2":
            if stok_sekarang - jumlah < 0:
                print("Error: Update dibatalkan, stok tidak boleh menjadi negatif!")
            else:
                stok_baru = stok_sekarang - jumlah
                stok_dict[kode]['Stok'] = str(stok_baru)
                print("Update berhasil: Stok dikurangi.")
        else:
            print("Pilihan menu tidak valid.")
                
    except ValueError:
        print("Error: Masukkan nilai berupa angka untuk jumlah stok.")
            

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()