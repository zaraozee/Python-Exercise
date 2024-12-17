nilai_ujian = float(input("Masukkan nilai ujian: "))
kehadiran = int(input("Masukkan jumlah hari kehadiran: "))

# Menentukan nilai akhir berdasarkan dua kondisi
if nilai_ujian >= 75:
    if kehadiran >= 75:
        nilai_akhir = "A"
    else:
        nilai_akhir = "B"
else:
    if kehadiran >= 75:
        nilai_akhir = "C"
    else:
        nilai_akhir = "D"

print(f"Nilai akhir siswa adalah: {nilai_akhir}")

