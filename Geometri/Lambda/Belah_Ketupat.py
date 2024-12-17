def belahketupat():
    print('======================================')
    print('==========  BELAH KETUPAT  ===========')
    print('======================================')

    d1 = int(input('masukan diagonal 1 :'))
    d2 = int(input('masukan diagonal 2 :'))
    sisi = int(input('masukan sisi :'))

    luas = lambda d1,d2 : 1/2 * d1 * d2
    keliling = lambda s : 4 * s

    print("luasnya adalah = ",luas(d1,d2)," cm")
    print("kelilingnya adalah = ",keliling(sisi)," cm")

belahketupat()
