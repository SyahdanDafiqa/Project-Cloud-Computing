import sqlite3


def tambah_campaign():
    conn = sqlite3.connect("donasi.db")
    cursor = conn.cursor()

    nama = input("Nama campaign: ")
    target = int(input("Target donasi: "))

    cursor.execute(
        "INSERT INTO campaign (nama_campaign, target) VALUES (?, ?)",
        (nama, target)
    )

    conn.commit()
    conn.close()

    print("Campaign berhasil ditambahkan!")



def lihat_campaign():
    conn = sqlite3.connect("donasi.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM campaign")
    data = cursor.fetchall()

    print("\n=== DAFTAR CAMPAIGN ===")

    for row in data:
        print(f"ID: {row[0]} | {row[1]} | Target: Rp{row[2]}")

    conn.close()
