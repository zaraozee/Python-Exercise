print("\tHITUNG GAJI KARYAWAN")
print("------------------------------------")

n = int(input("Masukkan jumlah karyawan: "))

gaji_per_jam = 10000

# Inisialisasi total gaji semua karyawan
total_gaji = 0

for i in range(n):
    print(f"\nKaryawan {i+1}:")
    jam_kerja = int(input("Masukkan jumlah jam kerja: "))
    
    if jam_kerja <= 7:
        gaji = jam_kerja * gaji_per_jam
    else:
        gaji = (7 * gaji_per_jam) + ((jam_kerja - 7) * (1.5 * gaji_per_jam))
    
    print(f"Gaji karyawan {i+1}: Rp{gaji:,}")
    total_gaji += gaji

print(f"\nTotal gaji yang harus dibayarkan oleh perusahaan: Rp{total_gaji:,}")
