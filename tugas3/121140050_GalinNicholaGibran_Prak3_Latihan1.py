class AkunBank:
    listpel = 0

    def __init__(self, norek, customer, saldo):
        self.__norek = norek
        self.__customer = customer
        self.__saldo = saldo
        AkunBank.listpel += 1

    def lihat_saldo():
        print(f"{Akun1.__customer} memiliki saldo Rp {Akun1.__saldo}")

    def tarik_tunai():
        while True:
            tarik = int(input("Masukan jumlah nominal yang ingin ditarik : "))

            if tarik > Akun1.__saldo:
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                Akun1.__saldo -= tarik
                print("Saldo berhasil ditarik!")
                break
    
    def transfer():
        transfer = int(input("Masukan nominal yang ingin ditransfer : "))
        tujuan = int(input("Masukan no rekening tujuan : "))
        
        if tujuan == Akun2.__norek:
            Akun2.__saldo += transfer
            Akun1.__saldo -= transfer
            print(f"Transfer Rp.{transfer} ke {Akun2.__customer} sukses!")
        elif tujuan == Akun3.__norek:
            Akun3.__saldo += transfer
            Akun1.__saldo -= transfer
            print(f"Transfer Rp.{transfer} ke {Akun3.__customer} sukses!")
        else:
            print("No rekening tujuan tidak dikenal!")

    def lihat_menu():
        print("Selamat datang di Bank Jago")
        print(f"Halo {Akun1.__customer}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        n = int(input("Masukan nomor input : "))

        print()
        if n == 1:
            AkunBank.lihat_saldo()
        elif n == 2:
            AkunBank.tarik_tunai()
        elif n == 3:
           AkunBank.transfer()
        elif n == 4:
            exit(0)
 
        print()
        print()
        AkunBank.lihat_menu()

Akun1 = AkunBank(91203, "Galin Nichola", 120000000)
Akun2 = AkunBank(666, "Kareem", 6666666666)
Akun3 = AkunBank(999, "Angee", 9999999999)

AkunBank.lihat_menu()