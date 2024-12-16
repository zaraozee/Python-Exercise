nilai_pixel = int(input("Masukkan nilai hasil operasi pixel: "))

if nilai_pixel > 255:
    nilai_pixel = 255
elif nilai_pixel < 0:
    nilai_pixel = 0

print(f"\nNilai pixel setelah clipping: {nilai_pixel}")
