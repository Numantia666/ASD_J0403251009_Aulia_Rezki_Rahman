#===============================================================
#Praktikum 2
#Latihan 1
#===============================================================


#Variabel menyimpan data file

nama_file ="data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} # Inisialisasi data dictionary

    with open(nama_file,'r', encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(',')
            data_dict[nim] = {"nama" : nama, "nilai" : nilai }
        return data_dict
    
buka_data = baca_data(nama_file)
print("Jumlah data adalah", len(buka_data))

#============================================================
#Latihan 2
#============================================================

def tampilkan_data(data_dict):
    print("\n=== Daftar Mahasiswa")
    print(f"{'NIM' :<10} | {'NAMA' :<12} | {'NILAI' :>5}")
    print("="*32)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f'{nim:<10} | {nama:<12}| {int(nilai):>5}')

print(tampilkan_data(buka_data))

#==================================================================
#Latihan 3
#==================================================================

def cari_data(data_dict):
    nim_cari = input("Masukan NIM yang akan dicari: ").strip()


    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["Nama"]
        nilai = data_dict[nim_cari]["Nilai"]

        print(f'nim :{nim_cari}')
        print(f'nama :{nama}')
        print(f'nilai :{nilai}')


#=============================================================================
#Latihan 4
#=============================================================================
def ubah_data(data_dict):
    nim = input("Masukan nim mahasiswa yang ingin dicari datanya: ").strip()

    if nim not in data_dict:
        print("Nim tidak ditemukan. Update dibatalkan")

    
    try:
        nilai_lama = data_dict[nim]['nilai']
        nilai_baru = int(input("Masukan nilai baru 0-100: "))
        data_dict[nim]["nilai"] = nilai_baru

        print(f"Update berhasil")

    except ValueError:
        print('Masukan nilai yang berupa angka')


    if nilai_baru < 10 or nilai_baru > 100:
        print("Nilai harus direntang 0-100")


#Latihan 5

def simpan_data(nama_file, data_dict):

    with open(nama_file, "w", encoding="utf=8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]['nilai']
            file.write(f'{nim},{nama},{nilai}\n')

simpan_data(nama_file, buka_data)
print("\nData Berhasil Disimpan", nama_file)



#Latihan 6
def main():
    buka_data = baca_data(nama_file)

    while True:
        print("\n===MENU DATA MAHASISWA==")
        print("1. Tampilkan data mahasiswa")
        print("1. Tampilkan data mahasiswa")
        print("1. Tampilkan data mahasiswa")
        print("1. Tampilkan data mahasiswa")



        pilihan = input("Pilih menu:").strip() 


        if pilihan == "1":
            tampilkan_data(buka_data)
    
        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan =="3":
                ubah_data(buka_data)

        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data disimpan")

        elif pilihan == "0":
            print("Progam Selesai")
            break
        
        else:
            print("Pilihan tidak Valid")

if __name__ == "__main__" :
    main()

