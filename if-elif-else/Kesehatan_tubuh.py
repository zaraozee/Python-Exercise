bmi = float(input("Masukkan nilai BMI: "))
tekanan_darah = int(input("Masukkan nilai tekanan darah: "))
kadar_gula = float(input("Masukkan nilai kadar gula darah: "))

# Menentukan kategori kesehatan berdasarkan tiga kondisi
if bmi < 18.5:
    if tekanan_darah < 120:
        if kadar_gula < 100:
            kategori = "Sehat"
        else:
            kategori = "BMI Rendah, Tekanan Darah Normal, Gula Tinggi"
    else:
        if kadar_gula < 100:
            kategori = "BMI Rendah, Tekanan Darah Tinggi, Gula Normal"
        else:
            kategori = "BMI Rendah, Tekanan Darah Tinggi, Gula Tinggi"
elif 18.5 <= bmi <= 24.9:
    if tekanan_darah < 120:
        if kadar_gula < 100:
            kategori = "Sehat"
        else:
            kategori = "BMI Normal, Tekanan Darah Normal, Gula Tinggi"
    else:
        if kadar_gula < 100:
            kategori = "BMI Normal, Tekanan Darah Tinggi, Gula Normal"
        else:
            kategori = "BMI Normal, Tekanan Darah Tinggi, Gula Tinggi"
else:
    if tekanan_darah < 120:
        if kadar_gula < 100:
            kategori = "BMI Tinggi, Tekanan Darah Normal, Gula Normal"
        else:
            kategori = "BMI Tinggi, Tekanan Darah Normal, Gula Tinggi"
    else:
        if kadar_gula < 100:
            kategori = "BMI Tinggi, Tekanan Darah Tinggi, Gula Normal"
        else:
            kategori = "BMI Tinggi, Tekanan Darah Tinggi, Gula Tinggi"

print(f"Kategori kesehatan: {kategori}")
