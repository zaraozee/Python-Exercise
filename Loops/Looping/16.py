jumlah_baris = int(input("Masukkan jumlah baris segitiga: "))

# segitiga bintang bagian atas
for i in range(jumlah_baris):
    print(' ' * (jumlah_baris - i - 1) + '*' * (2 * i + 1))

# segitiga bintang bagian bawah
for i in range(jumlah_baris - 1, -1, -1):
    print(' ' * (jumlah_baris - i - 1) + '*' * (2 * i + 1))
