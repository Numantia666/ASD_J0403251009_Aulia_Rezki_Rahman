#===============================================
#Nama   : Aulia Rezki Rahman
#Nim    : J0403251009
#Kelas  : TPL A2
#===============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinisiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau dapa pada list 
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

class queue: #buat konstruktor untuk isisilaisiasi variabel front dan rear
    def __init__(self):
        return self.front is None
    
        self.front = None # nnode paling depan
        self.rear = None # Node paling belakang

    #membuat fungsi untuk menambahkan data baru pada bagian belakang
    def enqueue(self, data):
        NodeBaru = Node(data) 
       
        #Jika queue kosong, front dan rar menunjukan ke node yang sama
        if self.is_empty():
            self.front = NodeBaru
            self.rear = NodeBaru
            return
       
        #Jika queue kosong, maka letakan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = NodeBaru #letakan data baru pada setelahnya rear
        self.rear = NodeBaru # jadikan dara baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan / front
        data_hapus = self.front.data #lihat data paling depan
        #geser front ke node berikutnya
        self.front = self.front.next

        #Jika setelah front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None

        return data_hapus

    def tampilkan(self):
        current = self.front
        print("Front -> ", end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")


#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
