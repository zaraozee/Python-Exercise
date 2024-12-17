print("=========================")
print("Menghitung Energi Kinetik")
print("=========================")

massa = int(input("masukkan massa benda: "))
kecepatan = int(input("masukkan kecepatan benda: "))

Ek = 0.5 * massa * (kecepatan ** 2)

print(f"energi kinetik benda adalah : {Ek} joule")