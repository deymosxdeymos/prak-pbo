# Nama: Galin Nichola Gibran
# NIM: 121140050
# Kelas: RB

# class
class Me:
    # constructor and attribute
    def __init__(self, nama, nim, kelas, sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
    # method
    def print_nama(self):
        print("Nama: ", self.nama)
    def print_nim(self):
        print("NIM: ", self.nim)
    def print_kelas(self):
        print("Kelas PBO: ", self.kelas)
    def print_sks(self):
        print("Jumlah SKS: ", self.sks)
#object
object = Me("Galin Nichola Gibran", 121140050, "RB", 22)

object.print_nama()
object.print_nim()
object.print_kelas()
object.print_sks()