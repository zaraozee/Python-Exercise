nilai_uang = int(input("Masukkan nilai uang dalam kelipatan 25: ")) #contoh: 2275
pecahan = [1000, 500, 100, 50, 25]

# Menghitung jumlah pecahan untuk setiap nilai
jumlah_pecahan = {}

for p in pecahan:
    jumlah_pecahan[p] = nilai_uang // p
    nilai_uang = nilai_uang % p

print("\n--- Nilai Tukaran Pecahan ---")
for p in pecahan:
    if jumlah_pecahan[p] > 0:
        print(f"{jumlah_pecahan[p]} buah pecahan Rp{p}")

