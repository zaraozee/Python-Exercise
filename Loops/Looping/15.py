jumlah_baris = int(input("Masukkan jumlah baris segitiga: "))
for i in range(jumlah_baris):
    print(' ' * (jumlah_baris - i - 1) + '*' * (2 * i + 1))

jumlah = 6
for i in range(jumlah):
    print(" " * (jumlah-i), "* " *i)
