def prismasegiempat():
    print('=======================================')
    print('=========== PRISMA SEGIEMPAT ==========')
    print('=======================================')

    panjang = float(input("masukan panjang alas segiempat\t\t :"))
    lebar = float(input("masukan lebar alas segiempat\t\t :"))
    tinggi = float(input("masukan tinggi prisma\t\t :"))

    luas_alas = lambda p, l: p * l
    volume_prisma = lambda luas, t: luas * t

    alas = luas_alas(panjang, lebar)
    volume = volume_prisma(alas, tinggi)

    print(f"\n luas alas segiempat : {alas} cm")
    print(f"\n volume prisma segiempat : {volume} cm3")

prismasegiempat()