tinggi = float(input("Masukkan tinggi badan : "))
berat_badan = float(input("Masukkan berat badan : "))

tinggi_badan = tinggi / 100                          #rumus lain
bmi_ideal = 22                                       #bmi_ideal = 22
berat_badan_ideal = bmi_ideal * (tinggi_badan ** 2)  #berat_ideal = (bmi_ideal / 10000)*(tinggi ** 2)

# Menentukan apakah berat badan ideal atau tidak
if abs(berat_badan - berat_badan_ideal) <= 2:
    status = "ideal"
else:
    status = "tidak ideal"

print(f"\nTinggi badan: {tinggi_badan} cm")
print(f"Berat badan: {berat_badan} kg")
print(f"\nBerat badan ideal: {berat_badan_ideal:.2f} kg")
print(f"Pesan: Berat badan anda {status}")
