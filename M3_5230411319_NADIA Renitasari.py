# Membuat class daftar menu
class DaftarMenu:
    def _init_(self):
        self.makanan = []  # Inisialisasi list makanan
        self.minuman = []  # Inisialisasi list minuman

    # Fungsi untuk menambahkan menu makanan
    def tambah_makanan(self, nama_makanan):
        self.makanan.append(nama_makanan)
        print(f'Makanan "{nama_makanan}" berhasil ditambahkan.')

    # Fungsi untuk menambahkan menu minuman
    def tambah_minuman(self, nama_minuman):
        self.minuman.append(nama_minuman)
        print(f'Minuman "{nama_minuman}" berhasil ditambahkan.')

    # Fungsi untuk menampilkan daftar makanan
    def tampilkan_makanan(self):
        if not self.makanan:
            print("Daftar makanan kosong.")
        else:
            print("Daftar Makanan:")
            for i, makanan in enumerate(self.makanan, 1):
                print(f"{i}. {makanan}")

    # Fungsi untuk menampilkan daftar minuman
    def tampilkan_minuman(self):
        if not self.minuman:
            print("Daftar minuman kosong.")
        else:
            print("Daftar Minuman:")
            for i, minuman in enumerate(self.minuman, 1):
                print(f"{i}. {minuman}")

# Membuat instance dari class DaftarMenu
menu = DaftarMenu()

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("\n=== Pilihan Menu ===")
    print("1. Tampilkan Daftar Makanan")
    print("2. Tampilkan Daftar Minuman")
    print("3. Tambah Daftar")
    print("4. Keluar")

# Fungsi untuk menampilkan submenu tambah daftar (makanan/minuman)
def tambah_daftar_menu():
    while True:
        print("\n=== Tambah Daftar ===")
        print("1. Tambah Daftar Makanan")
        print("2. Tambah Daftar Minuman")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            tambah_daftar_makanan()  # Memanggil fungsi untuk menambah daftar makanan
        elif pilihan == '2':
            tambah_daftar_minuman()  # Memanggil fungsi untuk menambah daftar minuman
        elif pilihan == '3':
            break  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Fungsi untuk menambahkan beberapa makanan ke daftar
def tambah_daftar_makanan():
    while True:
        nama_makanan = input("Masukkan nama makanan (atau ketik 'selesai' untuk berhenti): ")
        if nama_makanan.lower() == 'selesai':
            break
        menu.tambah_makanan(nama_makanan)

# Fungsi untuk menambahkan beberapa minuman ke daftar
def tambah_daftar_minuman():
    while True:
        nama_minuman = input("Masukkan nama minuman (atau ketik 'selesai' untuk berhenti): ")
        if nama_minuman.lower() == 'selesai':
            break
        menu.tambah_minuman(nama_minuman)

# Fungsi utama untuk menjalankan program
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            menu.tampilkan_makanan()
        elif pilihan == '2':
            menu.tampilkan_minuman()
        elif pilihan == '3':
            tambah_daftar_menu()  # Menampilkan submenu tambah daftar
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program utama
main()