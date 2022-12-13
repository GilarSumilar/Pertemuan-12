list = {}

# Biar singkat
def hading():
    '''Fungsi hading'''
    print("|                               Daftar Mahasiswa                             |")
    print("-"*78)                 
    print("| No |       Nama      |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
    print("-"*78)

class mahasiswa():


    # Menambahkan data inputan 
    def tambah():
        print("Tambah data :\n")
        nama    = input("Nama           : ")
        nim     = int(input("NIM            : "))
        uts     = int(input("Nilai UTS      : "))
        uas     = int(input("Nilai UAS      : "))
        tugas   = int(input("Nilai Tugas    : "))
        akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
        list[nama] = [nim, tugas, uts, uas, akhir]

    # Menampilkan seluruh data 
    def lihat():
        if list.items():
            print("-"*78)
            hading() # Biar singkat
            i = 0
            for data in list.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                    .format(data[0][:13], data[1][0], data[1][2], data[1][3], data[1][1], data[1][4], no=i))
                print("-"*78)
        else:
            print("-"*78)
            hading() # Biar singkat
            print("|                       TIDAK ADA DATA! Silakan tambah data                  |")
            print("-"*78)
            
        # Menghapus inputan nama
    def hapus(nama):
        del list[nama]
        print("\nData {0} berhasil di hapus".format(nama))    
    
        # Mengubah data nama inputan
    def ubah(nama):
        if nama in list.keys():
            nim     = int(input("NIM            : "))
            uts     = int(input("Nilai UTS      : "))
            uas     = int(input("Nilai UAS      : "))
            tugas   = int(input("Nilai Tugas    : "))
            akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
            list[nama] = [nim, tugas, uts, uas, akhir]
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))


        


print("="*20)
print("|PROGRAM INPUT DATA|")
print("="*20)

while True: 
    print()
    menu = input("[(T)ambah, (L)ihat, (H)apus, (U)bah, (K)eluar] : ")
    print("~"*78)
    print()

    if menu.lower() == 't':
        mahasiswa.tambah()

    elif menu.lower() == 'l':
        mahasiswa.lihat()       

    elif menu.lower() == "h":
        print("Masukan nama berdasarkan inputan")
        nama = str(input("\nMasukan Nama : "))
        if nama in list:
            mahasiswa.hapus(nama)


    elif menu.lower() == "u":
        nama = str(input("Masukan Nama : "))
        mahasiswa.ubah(nama) 

    elif menu.lower() == "k":
        print("Program selesai, Terima Kasih :) ")
        break

    else:
        print("\n INPUT {} TIDAK ADA!, Silakan pilih [T/L/H/U/K] untuk menjalankan program!".format(menu))