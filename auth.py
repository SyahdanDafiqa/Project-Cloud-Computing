import sqlite3
def register():
    conn = sqlite3.connect("donasi.db")
    cursor = conn.cursor()
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )
    conn.commit()
    conn.close()
    print("Register berhasil!")

def login():
    conn = sqlite3.connect("donasi.db")
    cursor = conn.cursor()
    username = input("Username: ")
    password = input("Password: ")
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login berhasil!")
        return True
    else:
        print("Login gagal!")
        return False