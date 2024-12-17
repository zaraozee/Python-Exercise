def persegipanjang():
    print('======================================')
    print('========== PERSEGI PANJANG ===========')
    print('======================================')

    panjang = float(input("masukan nilai panjang:"))
    lebar = float(input("masukan nilai lebar :"))

    luas = lambda panjang, lebar: panjang * lebar
    keliling = lambda panjang, lebar: 2 * (panjang + lebar)

    print("laus persegi panjang adalah:", luas(panjang, lebar), "cm" )
    print("keliling persegi panjang adalah:", keliling(panjang, lebar), "cm")

persegipanjang()

