def prismasegitiga():
    print('======================================')
    print('=========== PRISMA SEGITIGA ==========')
    print('======================================')

    alas = float(input("Masukkan panjang alas segitiga : "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga : "))
    tinggi_prisma = float(input("Masukkan tinggi prisma segitiga : "))

    hitung_luas_alas = lambda a, t: 0.5 * a * t
    hitung_volume = lambda luas, t: luas * t
    
    alas = hitung_luas_alas(alas, tinggi_segitiga)
    volume = hitung_volume(alas, tinggi_prisma)

    print(f"\nVolume prisma segitiga: {volume} cm3")
    print(f"Luas alas segitiga: {alas} cm")

prismasegitiga()
