jumlah = 0
nilai = 0

while nilai >= 0:
    nilai = int(input("Masukkan nilai : ")) #masukin nilai postif, habis itu nilai negatif(buat berhentiin) 
    if nilai >= 0:
        jumlah += nilai

print(f"Jumlah nilai yang dimasukkan: {jumlah}")
