print("Nama : Faizah Via Fadhillah")
print("Nim  : 312210460")

daftarkontak = {"Nama" : "Nomer Telepon"}
kontak = {'Ari': '081267888', 'Dina': '087677776'}


print("============================")
print("|   # Nama   |Nomor Telepon|")
print("============================")
print("|   # Ari    |  ", kontak['Ari'], '|')
print("|   # Dina   |  ", kontak['Dina'], '|')
print("============================")
print()


print(" Tampilkan kontaknya Ari")
print("===========================")
print("|    Ari     | ", kontak['Ari'], '|')
print("===========================")
print()


print(" Tambah kontak baru dengan nama Riko, nomor 087654544")
kontak['Riko'] = '087654544'
print("===========================")
print("|    Riko    | ", kontak['Riko'], '|')
print("===========================")
print()


print(" Ubah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print("===========================")
print("|    Dina    | ", kontak['Dina'], '|')
print("===========================")
print()


print(" Tampilkan semua Nama")
print("==================================")
print(kontak.keys())
print("==================================")
print()


print(" Tampilkan semua Nomor")
print("====================================================")
print(kontak.values())
print("====================================================")
print()


print(" Tampilkan daftar Nama dan nomornya")
print("================================================================================")
print(kontak.items())
print("================================================================================")
print()


print(" Hapus kontak Dina")
print("=========================================================")
kontak.pop('Dina')
print(kontak.items())
print("=========================================================")