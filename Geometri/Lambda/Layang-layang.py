def layang2():
    print('======================================')
    print('=========== LAYANG-LAYANG ============')
    print('======================================')

    sisi1 = int(input("masukan nilai sisi 1 :"))
    sisi2 = int(input("masukan nilai sisi 2 :"))
    diagonal1 = int(input("masukan nilai diagonal 1 :"))
    diagonal2 = int(input("masukan nilai diagonal 2 :"))

    luas = lambda s1,s2 : 2 * (s1+s2)
    keliling = lambda d1,d2 : 1/2 * (d1 * d2)

    print("luasnya adalah = ",luas(diagonal1,diagonal2), "cm" )
    print("kelilingnya adalah = ", keliling(sisi1,sisi2), "cm")

layang2()