# a
n = int(input("Masukkan bilangan bulat positif (1-10): "))

if 1 <= n <= 10:
    if n == 1:
        print("I")
    elif n == 2:
        print("II")
    elif n == 3:
        print("III")
    elif n == 4:
        print("IV")
    elif n == 5:
        print("V")
    elif n == 6:
        print("VI")
    elif n == 7:
        print("VII")
    elif n == 8:
        print("VIII")
    elif n == 9:
        print("IX")
    elif n == 10:
        print("X")
else:
    print("Bilangan tidak dalam rentang 1-10")


# b) mengonversi bilangan bulat positif sembarang ke angka Romawi
def konversi_ke_romawi(n):
    angka_romawi = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    hasil = ""
    for angka, simbol in angka_romawi:
        while n >= angka:
            hasil += simbol
            n -= angka
    return hasil

n = int(input("Masukkan bilangan bulat positif: "))

hasil_romawi = konversi_ke_romawi(n)
print(f"Angka Romawi: {hasil_romawi}")



