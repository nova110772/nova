from abc import ABC, abstractmethod
from typing import List

class LoggableMixin:
    def log(self, message: str):
        print(f"[LOG {self.__class__.__name__}] {message}")

class SearchableMixin:
    def matches(self, keyword: str) -> bool:
        return keyword.lower() in self.get_judul().lower() or keyword.lower() in self.get_id().lower()

class AbstractBuku(ABC):
    @abstractmethod
    def tampilkan_info(self): pass
    @abstractmethod
    def pinjam(self): pass
    @abstractmethod
    def kembalikan(self): pass
    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float: pass
    @abstractmethod
    def get_id(self) -> str: pass
    @abstractmethod
    def get_judul(self) -> str: pass

class Buku(AbstractBuku, LoggableMixin, SearchableMixin):
    def __init__(self, id_buku: str, judul: str, penulis: str, stok: int):
        self.__id_buku = id_buku
        self._judul = judul
        self.__penulis = penulis
        self.__stok = stok
        self.log(f"Buku dibuat: {judul}")

    def get_id(self) -> str: return self.__id_buku
    def get_judul(self) -> str: return self._judul

    def tampilkan_info(self):
        print(f"ID: {self.get_id()} | Judul: {self.get_judul()} | Penulis: {self.__penulis} | Stok: {self.__stok}")

    def pinjam(self):
        if self.__stok > 0:
            self.__stok -= 1
            self.log(f"Buku '{self.get_judul()}' dipinjam")
            return True
        self.log(f"Buku '{self.get_judul()}' habis stok!")
        return False

    def kembalikan(self):
        self.__stok += 1
        self.log(f"Buku '{self.get_judul()}' dikembalikan")

    def hitung_denda(self, hari_terlambat: int) -> float:
        return hari_terlambat * 5000  # Rp5.000 per hari

class BukuFiksi(Buku):
    def __init__(self, id_buku: str, judul: str, penulis: str, stok: int, genre: str):
        super().__init__(id_buku, judul, penulis, stok)
        self.__genre = genre

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"   Genre: {self.__genre}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        return super().hitung_denda(hari_terlambat) * 1.2  # denda lebih tinggi untuk fiksi

class BukuNonFiksi(Buku):
    def __init__(self, id_buku: str, judul: str, penulis: str, stok: int, edisi: int):
        super().__init__(id_buku, judul, penulis, stok)
        self.__edisi = edisi

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"   Edisi: {self.__edisi}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        return super().hitung_denda(hari_terlambat) * 0.8  # denda lebih rendah untuk non-fiksi

class Perpus(LoggableMixin):
    def __init__(self):
        self.__daftar_buku: List[AbstractBuku] = []
        self.log("Sistem Perpustakaan diinisialisasi")

    def tambah_buku(self, buku: AbstractBuku):
        self.__daftar_buku.append(buku)
        self.log(f"Buku ditambahkan: {buku.get_judul()}")

    def hapus_buku(self, id_buku: str):
        self.__daftar_buku = [b for b in self.__daftar_buku if b.get_id() != id_buku]
        self.log(f"Buku ID {id_buku} dihapus")

    def cari_buku(self, keyword: str) -> List[AbstractBuku]:
        results = [b for b in self.__daftar_buku if b.matches(keyword)]
        self.log(f"Pencarian '{keyword}' menemukan {len(results)} buku")
        return results

    def pinjam_buku(self, id_buku: str):
        for buku in self.__daftar_buku:
            if buku.get_id() == id_buku:
                return buku.pinjam()
        self.log(f"Buku ID {id_buku} tidak ditemukan")
        return False

    def kembalikan_buku(self, id_buku: str):
        for buku in self.__daftar_buku:
            if buku.get_id() == id_buku:
                buku.kembalikan()
                return True
        return False

    def laporan_perpus(self):
        self.log("Menghasilkan laporan perpustakaan")
        print("\n=== LAPORAN PERPUSTAKAAN ===")
        total_buku = 0
        for buku in self.__daftar_buku:
            buku.tampilkan_info()
            total_buku += 1
        print(f"\nTotal Buku Tersedia: {total_buku}")

if __name__ == "__main__":
    perpus = Perpus()
    perpus.tambah_buku(BukuFiksi("B001", "Harry Potter", "J.K. Rowling", 5, "Fantasi"))
    perpus.tambah_buku(BukuNonFiksi("B002", "Python OOP", "Mark Lutz", 10, 3))
    perpus.pinjam_buku("B001")
    perpus.laporan_perpus()