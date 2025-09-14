print("Nama     : Claudya Yusfa Ariyani")
print("NIM      : 2509116043")
print("--------------------------------")

print("Reservasi Kursi Bioskop")
print("-----------------------")

# List
reservasi_kursi = []

while True:
    print("\n Reservasi Kursi Bioskop")
    print("1. Membuat Reservasi Kursi")
    print("2. Mengubah Reservasi Kursi")
    print("3. Menghapus Reservasi Kursi")
    print("4. Keluar")

    menu_reservasi = input("Pilih Menu 1/2/3/4: ")

    if menu_reservasi == "1":
        nama = input("Nama Pemesan: ")
        kursi_kosong = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        print(kursi_kosong)
        pilih_kursi = input ("Pilih Kursi: ")
        print(nama)
        print(pilih_kursi)
        reservasi_kursi.append((nama, pilih_kursi))
        print("Kursi Berhasil Direservasi!")

    elif menu_reservasi == "2":
        if reservasi_kursi:
            pilih_kursi = input("Pilih Kursi Baru: ")
            print("Kursi telah diubah!")
        else:
            print("Tidak ada data yang diubah")

    elif menu_reservasi == "3":
        if reservasi_kursi:
            reservasi_kursi.clear()
            print("Kursi berhasil dihapus!")
        else:
            print("Tidak ada kursi untuk dihapus")

    elif menu_reservasi == "4":
        print("Keluar dari Program")
        break

    else:
        print("Menu tidak tersedia")
