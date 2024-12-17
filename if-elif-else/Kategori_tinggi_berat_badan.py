tinggi_badan = float(input("Masukkan tinggi badan : "))
berat_badan = float(input("Masukkan berat badan : "))
usia = int(input("Masukkan usia : "))

if tinggi_badan < 150:
    if berat_badan < 50:
        if usia < 12:
            kategori = "Anak-anak"
        elif 12 <= usia < 18:
            kategori = "Remaja"
        else:
            kategori = "Dewasa Pendek"
    else:
        if usia < 12:
            kategori = "Anak-anak dengan Berat Berlebih"
        elif 12 <= usia < 18:
            kategori = "Remaja dengan Berat Berlebih"
        else:
            kategori = "Dewasa Pendek dengan Berat Berlebih"
else:
    if berat_badan < 70:
        if usia < 18:
            kategori = "Remaja"
        elif 18 <= usia < 35:
            kategori = "Dewasa Muda"
        else:
            kategori = "Dewasa"
    else:
        if usia < 18:
            kategori = "Remaja dengan Berat Berlebih"
        elif 18 <= usia < 35:
            kategori = "Dewasa Muda dengan Berat Berlebih"
        else:
            kategori = "Dewasa dengan Berat Berlebih"

print(f"Kategori: {kategori}")
