def is_even(angka):
    return angka % 2 == 0

angka = int(input("Masukkan bilangan bulat: "))
if is_even(angka):
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")
