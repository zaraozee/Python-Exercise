print("\tSELISIH WAKTU")
print("----------------------------")

jam_mulai = int(input("Masukkan jam mulai (0-23): "))
menit_mulai = int(input("Masukkan menit mulai (0-59): "))
jam_selesai = int(input("Masukkan jam selesai (0-23): "))
menit_selesai = int(input("Masukkan menit selesai (0-59): "))

total_mulai = jam_mulai * 60 + menit_mulai
total_selesai = jam_selesai * 60 + menit_selesai

selisih_menit = total_selesai - total_mulai

# jika selisih negatif, tambahkan 24 jam (1440 menit)
if selisih_menit < 0:
    selisih_menit += 1440

# mengonversi selisih waktu kembali ke jam dan menit
selisih_jam = selisih_menit // 60
sisa_menit = selisih_menit % 60

print("\n--- Selisih Waktu ---")
print(f"Selisih waktu: {selisih_jam} jam {sisa_menit} menit")

