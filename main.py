class Kasir:
    def _init_(self):  # Perbaikan di sini
        self.keranjang = []

    def tampilkan_menu(self):
        print("===== MENU KASIR =====")
        print("1. Tambah Barang")
        print("2. Lihat Keranjang")
        print("3. Hapus Barang")
        print("4. Checkout")
        print("5. Keluar")
        print("======================")
