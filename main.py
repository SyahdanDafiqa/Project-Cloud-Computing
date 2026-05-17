from auth import register, login
from campaign import tambah_campaign, lihat_campaign
from donation import donasi
from report import laporan


while True:
    print("\n=== SISTEM DONASI ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        register()

    elif pilih == "2":
        if login():
            while True:
                print("\n=== MENU UTAMA ===")
                print("1. Tambah Campaign")
                print("2. Lihat Campaign")
                print("3. Donasi")
                print("4. Laporan")
                print("5. Logout")

                menu = input("Pilih menu: ")

                if menu == "1":
                    tambah_campaign()

                elif menu == "2":
                    lihat_campaign()

                elif menu == "3":
                    donasi()

                elif menu == "4":
                    laporan()

                elif menu == "5":
                    break

                else:
                    print("Menu tidak tersedia")

    elif pilih == "3":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")