barang1 = 20000
barang2 = 50000
barang3 = 40000
barang4 = 120000

total_belanja = barang1 + barang2 + barang3 + barang4
persentase_diskon = 7.5 / 100

# Hitung diskon jika total belanja minimal 200000
if total_belanja >= 200000:
    diskon = total_belanja * persentase_diskon
else:
    diskon = 0

total_bayar = total_belanja - diskon

print(f"Total Belanja : {total_belanja}")
print(f"Diskon        : {diskon}")
print(f"Total Bayar   : {total_bayar}")