# =========================================
# Praktikum 3: Mengubah Adjacency Matrix menjadi Adjacency List
# Nama      : Aulia Rezki Rahman
# NIM       : J0403251009 
# Kelas     : TPL A P2
# =========================================

# Fungsi untuk mengubah adjacency matrix
# menjadi adjacency list
def matrixToList(matrix):

    # Menentukan jumlah vertex
    n = len(matrix)

    # Membuat dictionary kosong
    adjList = {}

    # Perulangan untuk setiap baris matrix
    for i in range(n):

        # Membuat list kosong untuk menyimpan tetangga
        adjList[i] = []

        # Perulangan untuk setiap kolom
        for j in range(n):

            # Jika bernilai 1 berarti ada hubungan
            if matrix[i][j] == 1:

                # Menambahkan vertex yang terhubung
                adjList[i].append(j)

    # Mengembalikan adjacency list
    return adjList


# Program utama
if __name__ == "__main__":

    # Adjacency matrix
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    # Memanggil fungsi konversi
    adjList = matrixToList(matrix)

    # Menampilkan hasil adjacency list
    print("Adjacency List : ")

    # Perulangan untuk menampilkan isi adjacency list
    for key in adjList:

        # Menampilkan node
        print(f"{key} -> ", end=" ")

        # Menampilkan node yang terhubung
        for value in adjList[key]:
            print(value, end=" ")

        print()