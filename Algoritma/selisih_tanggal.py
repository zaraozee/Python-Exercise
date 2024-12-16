tahun = 365
bulan = 30

hari1 = int(input("Masukkan hari taggal pertama: "))
bulan1 = int(input("masukkan bulan tanggal pertama: "))
tahun1 = int(input("Masukkan tahun tanggal pertama: "))

print ("==============================")

hari2 = int(input("Masukkan hari tanggal kedua: "))
bulan2 = int(input("masukkan bulan tanggal kedua: "))
tahun2 = int(input("Masukkan tahun tanggal kedua: "))


total_hari1 = tahun1 * 365 + bulan1 * 30 + hari1
total_hari2 = tahun2 * 365 + bulan2 * 30 + hari2

selisih_hari = abs(total_hari2 - total_hari1)

tahun = selisih_hari // 365
sisa_hari = selisih_hari % 365
bulan = sisa_hari // 30
hari = sisa_hari % 30

print (f"\nselisih antara kedua tanggal adalah {tahun} tahun {bulan} bulan {hari} hari")
