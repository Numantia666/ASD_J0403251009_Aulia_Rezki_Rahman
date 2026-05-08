# =========================================
# Praktikum 1: Membuat Adjacency Matrix Graph
# Nama      : Aulia Rezki Rahman
# NIM       : J0403251009 
# Kelas     : TPL A P2
# =========================================

# Fungsi untuk membuat graph dalam bentuk adjacency matrix
def createGraph(v, edges):

    # Berfungsi untuk membuat matrix berukuran v x v
    # Agar semua isi awal bernilai 0
    # Nilai 0 berarti belum ada hubungan antar vertex
    mat = [[0 for _ in range(v)] for _ in range(v)]

    # Kode perulangan untuk membaca setiap edge
    for it in edges:

        # Kode mengambil vertex awal
        u = it[0]

        # Kode mengambil vertex tujuan
        v = it[1]

        # Mengisi nilai 1 pada posisi [u][v]
        # Tujuannya agar vertex u terhubung ke vertex v
        mat[u][v] = 1

        # Karena graph tidak memiliki arah,
        # maka hubungan berlaku timbal balik atau dua arah
        # maka demikian [v][u] juga bernilai 1
        mat[v][u] = 1

    # Mengembalikan nilai adjacency matrix
    return mat


# Program utama
if __name__ == "__main__":

    # Jumlah vertex atau node
    v = 4

    # Daftar edge atau sisi pada graph
    # Format: [vertex_awal, vertex_tujuan]
    edges = [
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 3]
    ]

    # Kode memanggil fungsi createGraph
    # Bertujuan untuk membuat adjacency matrix
    mat = createGraph(v, edges)

    # Menampilkan judul output
    print("Adjacency Matrix : ")

    # Perulangan untuk menampilkan baris matrix
    for i in range(v):

        # Perulangan untuk menampilkan kolom matrix
        for j in range(v):

            # Menampilkan isi matrix
            print(mat[i][j], end = " ")

        # Pindah ke baris baru
        print()