data ={ }
while True :
    print()
    f = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:")
    print()

#untuk melihat list
    if f.lower() =="l":
        if data.items():
            print("Daftar Nilai")
            print('='*84)
            print(f"|{'NO':^4}|{'NIM':^20}|{'NAMA':^20}|{'UTS':^10}|{'UAS':^6}|{'TUGAS':^6}|{'AKHIR':^10}|")
            print('='*84)
            i=0
            for x in data.items():
                i+=1
                print("|{no:^4}|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}|"
                      .format(x[0],x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],no=i))
                print('='*84)
        else :
            print("Daftar Nilai")
            print()
            print('='*79)
            print(f"|{'NIM':^20}|{'NAMA':^20}|{'UTS':^10}|{'UAS':^6}|{'TUGAS':^6}|{'AKHIR':^10}|")
            print('='*79)
            print(f"|{'TIDAK ADA DATA':^77}|")
            print('='*79)

# Untuk menambahkan data
    elif f.lower() == "t":
        print ("Tambah Data")
        nim   = int(input("NIM           : "))
        nama  = input    ("Nama          : ")
        uts   = int(input("Nilai UTS     : "))
        uas   = int(input("Nilai UAS     : "))
        tugas = int(input("Nilai Tugas   : "))
        akhir  = ((uts)*35/100+(uas)*35/100+(tugas)*30/100)
        data[nama] = nim, tugas, uts, uas, akhir

# Untuk mengubah data      
    elif f.lower() == "u":
        print("Edit Daftar Nilai")
        nama = input         (" Masukan Nama:")
        if nama in data.keys():
            nim   = input    ("Nim               :")
            uts   = int(input("Nilai UTS Baru    : "))
            uas   = int(input("Nilai UAS Baru    : "))
            tugas = int(input("Nilai Tugas Baru  : "))
            akhir  = ((uts)*35/100+(uas)*35/100+(tugas)*30/100)
            data[nama] = nim, tugas, uts, uas, akhir
        else :
            print("Daftar nilai{0} tidak ada ".format(nama))

# Untuk menghapus data
    elif f.lower() == "h":
        print("Hapus Daftar Nilai")
        nama = input(" Masukan Nama:")
        if nama in data.keys():
            del data[nama]
        else :
            print("Data {0} tidak ada".format(nama))  

# Untuk Mencari data
    elif f.lower() == "c":
        print("Cari Daftar Nilai")
        nama = input(" Masukan Nama: ")
        if nama in data.keys():
            print("Daftar Nilai")
            print('='*79)
            print(f"|{'NIM':^20}|{'NAMA':^20}|{'UTS':^10}|{'UAS':^6}|{'TUGAS':^6}|{'AKHIR':^10}|")
            print('='*79)
            print("|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}|" .format( nim, nama, uts, uas, tugas, akhir))
            print('='*79)
        else:
            print("Datanya {0} tidak ada ".format(nama))
            print("Daftar Nilai")
            print('='*79)
            print(f"|{'NIM':^20}|{'NAMA':^20}|{'UTS':^10}|{'UAS':^6}|{'TUGAS':^6}|{'AKHIR':^10}|")
            print('='*79)
            print(f"|{'TIDAK ADA DATA':^82}|")
            print('='*79)

# Untuk keluar dari program
    elif f.lower() == "k":
        print("Keluar dari program")
        break

    else:
        print("Pilih Tindakan Yang Tersedia")
              
        
            
          
           
        