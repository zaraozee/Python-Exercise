print ("==============================")
print ("====GEOMETRI  JAJARGENJANG====")
print ("==============================")

def jajargenjang():
    a = int(input("masukan alasnya : "))
    t = int(input("masukkan tingginya :"))
    s = int(input("masukan sisinya :"))
    p = int(input("masukan panjangnya: "))

    luas = lambda a,t : a * t
    keliling = lambda p,s : p*s

    print("luas jajargenjang = ", luas(a,t), "cm")
    print("Keliling jajargenjang = ", keliling(p,s), "cm")
jajargenjang()