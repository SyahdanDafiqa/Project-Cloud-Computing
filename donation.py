import sqlite3

def donasi():
    conn = sqlite3.connect("donasi.db")
    cursor = conn.cursor()

    nama = input("Nama donatur: ")
    campaign_id = int(input("ID campaign: "))
    nominal = int(input("Nominal donasi: "))

    cursor.execute(
        "INSERT INTO donasi (nama_donatur, campaign_id, nominal) VALUES (?, ?, ?)",
        (nama, campaign_id, nominal)
    )

    conn.commit()
    conn.close()

    print("Donasi berhasil!")
