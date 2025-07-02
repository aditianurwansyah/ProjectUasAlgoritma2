class Stack:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size

    def push(self, item): 
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            print(f"Item '{item}' ditambahkan ke stack.")
        else:
            print("Stack penuh! Tidak dapat menambahkan item.")

    def pop(self):
        if self.stack:
            removed_item = self.stack.pop()
            print(f"Item '{removed_item}' dihapus dari stack.")
        else:
            print("Stack kosong! Tidak ada item yang dapat dihapus.")

    def display(self):
        if self.stack:
            print("\nStack saat ini:")
            for item in reversed(self.stack):
                print(f"| {item} |")
            print("------")
        else:
            print("\nStack kosong.")

# Program utama
stack = Stack()

while True:
    print("\nMenu:")
    print("1. Push (Tambahkan item)")
    print("2. Pop (Hapus item)")
    print("3. Tampilkan Stack")
    print("4. Keluar")
    
    pilihan = input("Pilih opsi (1-4): ")
    
    if pilihan == "1":
        item = input("Masukkan item: ")
        stack.push(item)
    elif pilihan == "2":
        stack.pop()
    elif pilihan == "3":
        stack.display()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
