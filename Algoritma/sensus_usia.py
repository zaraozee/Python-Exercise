jumlah_penduduk = int(input("Masukkan jumlah penduduk: "))
usia_penduduk = []

# Memasukkan data usia untuk setiap penduduk
for i in range(jumlah_penduduk):
    usia = int(input(f"Masukkan usia penduduk ke-{i + 1}: "))
    usia_penduduk.append(usia)

# Menghitung rata-rata usia
rata_rata_usia = sum(usia_penduduk) / jumlah_penduduk

# usia tertua pertama dan kedua
usia_penduduk_sorted = sorted(usia_penduduk, reverse=True)
tertua1 = usia_penduduk_sorted[0]
tertua2 = usia_penduduk_sorted[1]

# usia termuda pertama dan kedua
termuda1 = usia_penduduk_sorted[-1]
termuda2 = usia_penduduk_sorted[-2]

# Menghitung jumlah penduduk untuk setiap usia
usia_count = {}
for usia in usia_penduduk:
    if usia in usia_count:
        usia_count[usia] += 1
    else:
        usia_count[usia] = 1

print("\n--- Hasil Sensus Usia ---")
print(f"Rata-rata usia: {rata_rata_usia} tahun")
print(f"Usia tertua pertama: {tertua1} tahun")
print(f"Usia tertua kedua: {tertua2} tahun")
print(f"Usia termuda pertama: {termuda1} tahun")
print(f"Usia termuda kedua: {termuda2} tahun")

print("\nJumlah penduduk untuk masing-masing usia:")
for usia, count in usia_count.items():
    print(f"Usia {usia}: {count} orang")

# Contoh hasil
# Input:
# Masukkan jumlah penduduk: 5
# Masukkan usia penduduk ke-1: 25
# Masukkan usia penduduk ke-2: 30
# Masukkan usia penduduk ke-3: 22
# Masukkan usia penduduk ke-4: 25
# Masukkan usia penduduk ke-5: 30
# Output:
# Rata-rata usia: 26.40 tahun
# Usia tertua pertama: 30 tahun
# Usia tertua kedua: 30 tahun
# Usia termuda pertama: 22 tahun
# Usia termuda kedua: 25 tahun
# Jumlah penduduk untuk masing-masing usia:
# Usia 25: 2 orang
# Usia 30: 2 orang
# Usia 22: 1 orang
