import re  

users = {}

def validate_password(password):
    if len(password) < 8:
        print("Password minimal harus 8 karakter.")
        return False
    
    if not re.search(r"[A-Z]", password):
        print("Password harus mengandung minimal satu huruf kapital.")
        return False
    
    if not re.search(r"\d", password):
        print("Password harus mengandung minimal satu angka.")
        return False
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password harus mengandung minimal satu simbol (seperti !, @, #, $, dll.).")
        return False
    
    return True

def register():
    print("\n=== Register ===")
    
    username = input("Masukkan username: ")
    
    if username == "":
        print("Username tidak boleh kosong!")
        return
    
    if username in users:
        print("Username sudah terdaftar. Silakan pilih username lain.")
        return
    
    password = input("Masukkan password: ")
    
    if not validate_password(password):
        return
    
    users[username] = password
    print(f"Registrasi berhasil! Selamat datang, {username}.")

def login():
    print("\n=== Login ===")
    
    username = input("Masukkan username: ")
    
    if username not in users:
        print("Username tidak ditemukan. Silakan register terlebih dahulu.")
        return
    
    password = input("Masukkan password: ")
    
    if users[username] == password:
        print(f"Login berhasil! Selamat datang kembali, {username}.")
    else:
        print("Password salah!")

def main_menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

main_menu()