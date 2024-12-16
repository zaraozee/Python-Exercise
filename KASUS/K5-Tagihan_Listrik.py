print("\tTAGIHAN LISTRIK")
print("--------------------------------")

golongan = int(input("Masukkan golongan tarif (1 atau 2): "))
kwh_pemakaian = int(input("Masukkan pemakaian listrik dalam kWh: "))

# Menentukan tarif berdasarkan golongan
if golongan == 1:
    tarif = 1000
elif golongan == 2:
    tarif = 2000
else:
    print("Golongan tidak valid. Silakan masukkan golongan 1 atau 2.")
    exit()

if kwh_pemakaian < 100:
    kwh_pemakaian = 100  # Minimum pembayaran adalah untuk 100 kWh
biaya = kwh_pemakaian * tarif

# Menambahkan 10% jika pemakaian 1000 kWh atau lebih
if kwh_pemakaian >= 1000:
    biaya += 0.10 * biaya

print(f"\n--- Rincian Tagihan Listrik ---")
print(f"Golongan tarif: {golongan}")
print(f"Pemakaian listrik: {kwh_pemakaian} kWh")
print(f"Total tagihan: Rp{biaya:,}")
