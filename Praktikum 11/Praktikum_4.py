# =========================================
# PRAKTIKUM 4 REPRESENTASI GRAPH
# STUDI KASUS JARINGAN KOMPUTER
# Nama : Aulia Rezki Rahman
# NIM  : J0403251009
# Kelas: TPL A P2
# =========================================

# Daftar nama node
nodes = [
    "Router",
    "Switch1",
    "Switch2",
    "Server",
    "PC1",
    "PC2",
    "AccessPoint"
]

# Daftar edge/koneksi
edges = [
    [0,1],
    [0,2],
    [1,4],
    [1,5],
    [2,3],
    [2,6]
]

# =========================================
# MEMBUAT ADJACENCY MATRIX
# =========================================

def createMatrix(v, edges):

    # Membuat matrix kosong
    matrix = [[0 for _ in range(v)] for _ in range(v)]

    # Mengisi hubungan antar node
    for edge in edges:

        u = edge[0]
        w = edge[1]

        matrix[u][w] = 1
        matrix[w][u] = 1

    return matrix


# =========================================
# MEMBUAT ADJACENCY LIST
# =========================================

def createList(v, edges):

    # Membuat dictionary kosong
    adjList = {i: [] for i in range(v)}

    # Mengisi hubungan node
    for edge in edges:

        u = edge[0]
        w = edge[1]

        adjList[u].append(w)
        adjList[w].append(u)

    return adjList


# Jumlah node
v = len(nodes)

# Membuat adjacency matrix
matrix = createMatrix(v, edges)

# Membuat adjacency list
adjList = createList(v, edges)

# =========================================
# OUTPUT ADJACENCY LIST
# =========================================

print("ADJACENCY LIST")
print()

for i in range(v):

    print(nodes[i], "-> ", end="")

    for j in adjList[i]:
        print(nodes[j], end="  ")

    print()

# =========================================
# OUTPUT ADJACENCY MATRIX
# =========================================

print("\nADJACENCY MATRIX")
print()

# Header kolom
print("      ", end="")

for name in nodes:
    print(f"{name[:4]:<6}", end="")

print()

# Isi matrix
for i in range(v):

    print(f"{nodes[i][:4]:<6}", end="")

    for j in range(v):
        print(f"{matrix[i][j]:<6}", end="")

    print()