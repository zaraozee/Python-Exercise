print("\tBIAYA PARKIR")
print("----------------------------")

jam_masuk = int(input("Masukkan jam masuk (0-24): "))
jam_keluar = int(input("Masukkan jam keluar (0-24): "))

if 0 <= jam_masuk < 24 and 0 <= jam_keluar < 24 and jam_keluar > jam_masuk:
    # Menghitung lama parkir
    lama_parkir = jam_keluar - jam_masuk
    
    # Menghitung biaya parkir
    if lama_parkir <= 2:
        biaya_parkir = 2000
    else:
        biaya_parkir = 2000 + (lama_parkir - 2) * 500
    print(f"Biaya parkir: Rp{biaya_parkir}")
else:
    print("Jam masuk dan jam keluar tidak valid. Silakan coba lagi.")
