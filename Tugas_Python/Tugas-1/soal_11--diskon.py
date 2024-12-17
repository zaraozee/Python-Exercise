jumlah = int(input("masukan total harga pembelian :"))

if (jumlah >= 100000):
    a = jumlah * 5 / 100
    print("kamu mendapatkan diskon 5% :", int(a))

else:
    a = jumlah * 0
    print("barang tidak mendapat diskon :", int(a))
    b = jumlah - a
    print("jumlah yang harus dibayar :", int(b)) 