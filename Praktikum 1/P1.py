#==================================================================
#Praktikum 1 : Konsep HDT dan File Handling
#Latihan dasar : Membaca seluruh isi data
#==================================================================

print('=====Membuka File dalam Satu String=====')
with open('data_mahasiswa.txt', 'r', encoding= 'utf-8') as file:
    isi_file = file.read()
print(isi_file)
print('Tipe data: ',type(isi_file))

#==================================================================
#Praktikum 1 : Konsep HDT dan File Handling
#Latihan dasar 2 : membaca seluruh isi file data dengan cara per baris
#==================================================================


print('==========Membuka file per baris===========')
jumlah_baris = 0 # Inisiasi variabel untuk menghitung jumlah baris
with open('data_mahasiswa.txt', 'r', encoding= 'utf-8') as file:
    for baris in file: 
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print('Baris ke', jumlah_baris)
        print('isinya', baris)


#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom data

with open('data_mahasiswa.txt', 'r', encoding= 'utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #Pecah menjadi data satuan dan diubah menjadi variabel
        print("Nim:", nim, "Nama", nama, "Nilai", nilai)


 
#==================================================================
#Praktikum 1 : Konsep HDT dan File Handling
#Latihan dasar 3 : Membaca data dan menyimpan ke struktrur list
#==================================================================


data_list = []
with open('data_mahasiswa.txt', 'r', encoding= 'utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") 
        data_list.append([nim, nama, int(nilai)])

print('Menampilkan list')
print(data_list)
print("Contoh record pertama", data_list[0])
print("Contoh record kedua", data_list[1])

print('Jumlah record', len(data_list))


 
#==================================================================
#Praktikum 1 : Konsep HDT dan File Handling
#Latihan dasar 4 : Membaca dan Menyimpan Struktur Data Dictionary
#==================================================================
data_dict = {}

with open('data_mahasiswa.txt', 'r', encoding= 'utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            "nama"  : nama,
            "nilai" : int(nilai),

        }

print("Tampilkan Data")
print(data_dict)