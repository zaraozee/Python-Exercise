nilai_uang = int(input("Masukkan nilai uang: "))

if 100 <= nilai_uang < 1000:
    kategori = "ratusan"
elif 1000 <= nilai_uang < 10000:
    kategori = "ribuan"
elif 10000 <= nilai_uang < 100000:
    kategori = "puluhan ribu"
elif 100000 <= nilai_uang < 1000000:
    kategori = "ratusan ribu"
elif nilai_uang >= 1000000:
    kategori = "jutaan"
else:
    kategori = "di bawah ratusan"

print(f"Uang sebesar {nilai_uang} termasuk dalam kategori {kategori}")


