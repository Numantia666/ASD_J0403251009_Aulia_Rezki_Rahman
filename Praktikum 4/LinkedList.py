#===============================================
#Nama   :  
#Nim    :
#Kelas  :
#===============================================

#===============================================
#Implementasi dasar : Node Pada Linked List
#===============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinisiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau dapa pada list 
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mendefinisikan head dan Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#===============================================
#Implementasi dasar : Stack
#===============================================

