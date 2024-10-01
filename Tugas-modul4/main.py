# Program Kasir Sederhana

def tampilkan_menu():
    print("===== MENU KASIR =====")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Hapus Barang")
    print("4. Checkout")
    print("5. Keluar")
    print("======================")

# List untuk menyimpan item belanjaan
keranjang = []

# Fungsi untuk menambahkan barang ke keranjang
def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang: "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total_harga = harga_barang * jumlah_barang
    keranjang.append({"nama": nama_barang, "harga": harga_barang, "jumlah": jumlah_barang, "total": total_harga})
    print(f"{nama_barang} berhasil ditambahkan ke keranjang.\n")

# Fungsi untuk menampilkan isi keranjang
def lihat_keranjang():
    if not keranjang:
        print("Keranjang belanja kosong.\n")
    else:
        print("===== KERANJANG BELANJA =====")
        for i, item in enumerate(keranjang, 1):
            print(f"{i}. {item['nama']} - {item['jumlah']} x Rp{item['harga']} = Rp{item['total']}")
        print("==============================\n")

# Fungsi untuk menghapus barang dari keranjang
def hapus_barang():
    lihat_keranjang()
    if keranjang:
        pilihan = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
        if 0 <= pilihan < len(keranjang):
            barang_terhapus = keranjang.pop(pilihan)
            print(f"{barang_terhapus['nama']} berhasil dihapus dari keranjang.\n")
        else:
            print("Nomor barang tidak valid.\n")

# Fungsi untuk checkout dan menghitung total
def checkout():
    if not keranjang:
        print("Keranjang belanja kosong.\n")
    else:
        total_belanja = sum(item["total"] for item in keranjang)
        print("===== STRUK PEMBAYARAN =====")
        lihat_keranjang()
        print(f"Total yang harus dibayar: Rp{total_belanja}")
        bayar = float(input("Masukkan jumlah uang yang dibayarkan: "))
        if bayar >= total_belanja:
            kembalian = bayar - total_belanja
            print(f"Pembayaran berhasil. Kembalian Anda: Rp{kembalian}\n")
            keranjang.clear()  # Mengosongkan keranjang setelah checkout
        else:
            print("Uang tidak cukup!\n")

# Program utama
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            lihat_keranjang()
        elif pilihan == "3":
            hapus_barang()
        elif pilihan == "4":
            checkout()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan kasir kami!")
            break
        else:
            print("Pilihan tidak valid.\n")

# Menjalankan program utama
if _name_ == "_main_":
    main()