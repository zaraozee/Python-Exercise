x = int(input("Masukkan bilangan bulat x: "))
y = int(input("Masukkan bilangan bulat y: "))
z = int(input("Masukkan bilangan bulat z: "))

# Mencari nilai terbesar
if x >= y and x >= z:
    nilai_terbesar = x
elif y >= x and y >= z:
    nilai_terbesar = y
else:
    nilai_terbesar = z

# Mencari nilai terkecil
if x <= y and x <= z:
    nilai_terkecil = x
elif y <= x and y <= z:
    nilai_terkecil = y
else:
    nilai_terkecil = z

print(f"Nilai terbesar adalah: {nilai_terbesar}")
print(f"Nilai terkecil adalah: {nilai_terkecil}")
