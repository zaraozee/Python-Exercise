def segitiga() :
    print('======================================')
    print('======== Menghitung Segitiga ========')
    print('======================================')

    alas = float(input("Masukkan panjang alas segitiga : "))
    tinggi = float(input("Masukkan tinggi segitiga : "))
    sisiA = float(input("Masukkan panjang sisi a : "))
    sisiB = float(input("Masukkan panjang sisi b : "))
    sisiC = float(input("Masukkan panjang sisi c : "))

    luas = lambda a,b,c : a + b + c
    keliling = lambda a,t : 1/2 * a * t

    print("Nilai Luas Persegi adalah\t= ", luas(sisiA,sisiB,sisiC), "cm")
    print("Nilai Keliling Persegi adalah\t= ", keliling(alas,tinggi), "cm")

segitiga()

