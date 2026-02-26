# =========================
# class Buku
# =========================
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.sedang_dipinjam = False

    def pinjam(self):
        self.sedang_dipinjam = True

    def kembalikan(self):
        self.sedang_dipinjam = False

# =========================
# class Anggota
# =========================
class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota

# =========================
# class Petugas
# =========================
class Petugas:
    def __init__(self, nama, id_petugas):
        self.nama = nama
        self.id_petugas = id_petugas

# =========================
# class TransaksiPeminjaman
# =========================
class TransaksiPeminjaman:
    def __init__(self, buku, anggota, petugas, tanggal_pinjam):
        self.buku = buku
        self.anggota = anggota
        self.petugas = petugas
        self.tanggal_pinjam = tanggal_pinjam
        self.sudah_dikembalikan = False

    def proses_pinjam(self):
        if not self.buku.sedang_dipinjam:
            self.buku.pinjam()
            print("Buku berhasil dipinjam")
            print("Status buku : Dipinjam")
        else:
            print("Buku sedang dipinjam")

    def proses_kembali(self):
        if self.buku.sedang_dipinjam:
            self.buku.kembalikan()
            self.sudah_dikembalikan = True
            print("Buku telah dikembalikan")
            print("Status buku : Tersedia")
        else:
            print("Buku belum dipinjam")

# =========================
# membuat objek
# =========================
print("=== sistem peminjaman buku ===")

buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
anggota1 = Anggota("Aisyah", "A001")
petugas1 = Petugas("Riski", "P001")

transaksi1 = TransaksiPeminjaman(
    buku1, anggota1, petugas1, "26-02-2026"
)

print("\nData Awal")
print("Judul Buku  :", buku1.judul)
print("Penulis    :", buku1.penulis)
print("Status     :", buku1.sedang_dipinjam)

print("\nProses Peminjaman")
transaksi1.proses_pinjam()

print("\nProses Pengembalian")
transaksi1.proses_kembali()