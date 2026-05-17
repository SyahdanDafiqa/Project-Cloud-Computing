import sqlite3

conn = sqlite3.connect("donasi.db")
cursor = conn.cursor()

# Tabel users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

# Tabel campaign
cursor.execute('''
CREATE TABLE IF NOT EXISTS campaign (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_campaign TEXT,
    target INTEGER
)
''')
# Tabel donasi
cursor.execute('''
CREATE TABLE IF NOT EXISTS donasi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_donatur TEXT,
    campaign_id INTEGER,
    nominal INTEGER
)
''')

conn.commit()
conn.close()

print("Database berhasil dibuat!")