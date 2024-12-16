tahun_hari = 365
bulan_hari = 30

hari1 = int(input("masukkan jumlah hari: "))
tahun = int(hari1 / tahun_hari)
hari2 = hari1 % tahun_hari
bulan = int (hari2 / bulan_hari)
hari = hari2 % bulan_hari

print (f"{tahun} tahun {bulan} bulan {hari} hari")