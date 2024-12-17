lembar_buku = int(input("jumlah lembar buku :"))

if lembar_buku > 40 and lembar_buku <= 45:
    print("banyak")
elif lembar_buku > 35 and lembar_buku <= 40:
    print("lumayan")
elif lembar_buku >= 30 and lembar_buku <= 35: 
    print("sedikit")
else:
    print("tidak ada")