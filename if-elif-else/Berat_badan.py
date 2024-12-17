berat = float(input("Masukkan berat badan : "))
tinggi = float(input("Masukkan tinggi badan : "))

bmi = berat / (tinggi ** 2)

# Menentukan kategori 
if bmi < 18.5:
    print("\tBerat badan kurang")
elif 18.5 <= bmi < 24.9:
    print ("\tBerat badan normal")
elif 25 <= bmi < 29.9:
    print("\tBerat badan lebih")
else:
    print("\tobesitas")
