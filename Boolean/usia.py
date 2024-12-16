def is_adult(age):
    return age >= 18

age = int(input("Masukkan usia: "))
if is_adult(age):
    print("usia kamu di atas 18 tahun.")
else:
    print("usia kamu di bawah 18 tahun.")
