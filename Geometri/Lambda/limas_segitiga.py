def limassegitiga():
    print ("==============================")
    print ("======= LIMAS SEGITIGA =======")
    print ("==============================")

    alas_segitiga = float(input("Masukkan panjang alas segitiga (dalam satuan): "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga (dalam satuan): "))
    tinggi_limas = float(input("Masukkan tinggi limas (dalam satuan): "))

    luas_alas = lambda a, t: 0.5 * a * t
    volume_limas = lambda luas, t: (1/3) * luas * t

    alas = luas_alas(alas_segitiga, tinggi_segitiga)
    volume = volume_limas(alas, tinggi_limas)

    print(f"\nLuas alas segitiga: {alas}")
    print(f"Volume limas segitiga: {volume} ")

limassegitiga()

