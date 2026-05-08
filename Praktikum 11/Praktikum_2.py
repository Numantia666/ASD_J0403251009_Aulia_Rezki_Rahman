# =========================================
# Praktikum 2: Membuat Adjacency List Graph
# Nama      : Aulia Rezki Rahman
# NIM       : J0403251009 
# Kelas     : TPL A P2
# =========================================

# Fungsi untuk membuat graph
def createGraph(edges):

    # Membuat dictionary kosong
    adjList = {}

    # Perulangan untuk membaca setiap bagian edge
    for u, v in edges:

        # Jika node u tidak ada di dictionary
        if u not in adjList:
            adjList[u] = []

        # Jika node v tidak ada di dictionary
        if v not in adjList:
            adjList[v] = []

        # Menambahkan hubungan u ke v
        adjList[u].append(v)

        # Karena graph tidak memiliki arah,
        # maka v juga terhubung ke u
        adjList[v].append(u)

    # Mengembalikan adjacency list
    return adjList


# Program utama
if __name__ == "__main__":

    # Daftar edge pada graph
    # A-B, A-C, B-D, C-D
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'D')
    ]

    # Membuat adjacency list
    adjList = createGraph(edges)

    # Menampilkan adjacency list
    print("Adjacency List : ")

    # Perulangan untuk menampilkan isi dictionary
    for node in adjList:

        # Menampilkan node
        print(f"{node} -> ", end=" ")

        # Menampilkan node yang terhubung
        for tetangga in adjList[node]:
            print(tetangga, end=" ")

        print()