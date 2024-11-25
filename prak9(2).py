def menu():
    print("===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Teks Pada File")
    print("4. Keluar Dari Program")

def buat_file():
    nama_file = input("Masukkan Nama File: ") + ".txt"
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan tahun angkatanmu: ")
    with open(nama_file, "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"NIM: {nim}\n")
        file.write(f"Angkatan: {angkatan}\n")
    print("\nFile Berhasil Dibuat\n")

def baca_file():
    nama_file = input("Masukkan Nama File: ") + ".txt"
    try:
        with open(nama_file, "r") as file:
            print("\nIsi File:")
            print(file.read())
    except FileNotFoundError:
        print("\nFile tidak ditemukan!\n")

def tambah_teks():
    nama_file = input("Masukkan Nama File: ") + ".txt"
    tambahan = input("Masukkan nama sahabatmu: ")
    try:
        with open(nama_file, "a") as file:
            file.write(tambahan + "\n")
        print("\nTeks Berhasil Ditambahkan\n")
    except FileNotFoundError:
        print("\nFile tidak ditemukan!\n")

while True:
    menu()
    pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")
    if pilihan == "1":
        buat_file()
    elif pilihan == "2":
        baca_file()
    elif pilihan == "3":
        tambah_teks()
    elif pilihan == "4":
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi!\n")

