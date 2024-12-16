print("\tJUMLAH MINIBUS")
print("----------------------------")

jumlah_peserta = int(input("Masukkan jumlah peserta: "))

kapasitas_minibus = 7

# menghitung jumlah minibus yang dibutuhkan
if jumlah_peserta % kapasitas_minibus == 0:
    jumlah_minibus = jumlah_peserta // kapasitas_minibus
else:
    jumlah_minibus = jumlah_peserta // kapasitas_minibus + 1

print(f"Jumlah minibus yang diperlukan: {jumlah_minibus}")
