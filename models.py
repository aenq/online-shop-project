import pymysql
import config

db = cursor = None

# TES AJA
# class Pengguna:
#     def __init__(self, nama_awal=None, nama_akhir=None, username=None,  alamat_rinci=None, kota=None, provinsi=None, kodepos=None, email=None,  password=None):
#         self.nama_awal = nama_awal
#         self.nama_akhir = nama_akhir
#         self.username = username
#         self.alamat_rinci = alamat_rinci
#         self.kota = kota
#         self.provinsi = provinsi
#         self.kodepos = kodepos
#         self.email = email
#         self.password = password

#     def openDB(self):
#         global db, cursor
#         db = pymysql.connect(
#             host=config.DB_HOST,           user=config.DB_USER,
#             password=config.DB_PASSWORD,
#             database=config.DB_NAME
#         )
#         cursor = db.cursor()

#     def closeDB(self):
#         global db, cursor
#         db.close()

#     def selectDB(self):
#         self.openDB()
#         cursor.execute("SELECT * FROM pengguna")
#         container = []
#         for nama_awal, nama_akhir, username, alamat_rinci, kota, provinsi, kodepos, email, password in cursor.fetchall():
#             container.append((nama_awal, nama_akhir, username,
#                              alamat_rinci, kota, provinsi, kodepos, email,  password))
#         self.closeDB()
#         return container


class Keranjang:
    def __init__(self, no=None, produk=None, paket=None, harga=None,  jumlah=None, subtotal=None):
        self.no = no
        self.produk = produk
        self.paket = paket
        self.harga = harga
        self.jumlah = jumlah
        self.subtotal = subtotal

    def openDB(self):
        global db, cursor
        db = pymysql.connect(
            host=config.DB_HOST,           user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        cursor = db.cursor()

    def closeDB(self):
        global db, cursor
        db.close()

    def selectDB(self):
        self.openDB()
        cursor.execute("SELECT * FROM keranjang")
        container = []
        for no, produk, paket, harga, jumlah, subtotal in cursor.fetchall():
            container.append((no, produk, paket, harga,
                             jumlah, subtotal))
        self.closeDB()
        return container
