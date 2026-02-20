#===============================================
#Nama   : Aulia Rezki Rahman
#Nim    : J0403251009
#Kelas  : TPL A2
#===============================================

#===============================================
#Implementasi dasar : Stack
#===============================================


class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinisiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau dapa pada list 
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#Satack ada operasi push(memasukkan head baru) dan pop(menghapushead)
#A -> B -> C -> None
# A -> B -> C->None

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None #stack kosong jika 

    def push(self, data):
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstraktor pada class Node

        #2 node baru harus menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru


    def pop(self): #mengambil / menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None

        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):#melihat data paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data



    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top " , end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi class Stack        
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
print("Peek (Lihat Top: )", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top: )", s.peek())