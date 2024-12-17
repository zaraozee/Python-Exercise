def limassegiempat():
    print ("==============================")
    print ("===GEOMETRI LIMAS SEGIEMPAT===")
    print ("==============================")
    
    panjang = float(input("Masukkan panjang alas segiempat : "))
    lebar = float(input("Masukkan lebar alas segiempat : "))
    tinggi_limas = float(input("Masukkan tinggi limas : "))

    luas_alas = lambda p, l: p * l
    volume_limas = lambda luas, t: (1/3) * luas * t

    alas = luas_alas(panjang, lebar)
    volume = volume_limas(alas, tinggi_limas)

    print(f"\nLuas alas segiempat: {alas} cm")
    print(f"Volume limas segiempat: {volume} cm3")

limassegiempat()

