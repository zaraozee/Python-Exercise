def kategorikan_angka(angka):
    if 100 <= angka < 1000:
        return "Ratusan"
    elif 1000 <= angka < 10000:
        return "Ribuan"
    elif 1000000 <= angka < 10000000:
        return "Jutaan"
    else:
        return "Tidak termasuk dalam kategori ratusan, ribuan, atau jutaan"

angka = int(input("Masukkan angka: "))

kategori = kategorikan_angka(angka)
print(f"Angka {angka} : {kategori}")
