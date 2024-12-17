def kerucut():
    print ("===================================")
    print ("======== GEOMETRI KERUCUT =========")
    print ("===================================")

    r = int(input("masukkan jari-jarinya: "))
    s = int(input("masukkan sisi kerucut: "))
    t = int(input("masukkan tinggi kerucut: "))

    PHI = 3.14
    s = lambda PHI, r, s: PHI * r * s
    lp = lambda PHI,r,s: (PHI * r * s) + (PHI * r * r)
    v = lambda PHI,r,t: 1/3 * PHI * r * r * t

    print('luas selimut\t: ',s, "cm")
    print('luas permukaan \t: ',lp)
    print('volume\t\t: ',round(v,2))
kerucut()