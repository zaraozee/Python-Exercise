tinggi = float(input("Masukkan tinggi badan (dalam cm): "))

berat_ideal_sementara = tinggi - 100
persentase = 0.1 * berat_ideal_sementara
berat_ideal = berat_ideal_sementara - persentase

print(f"\nBerat badan ideal untuk tinggi {tinggi} cm adalah {berat_ideal:.2f} kg")
