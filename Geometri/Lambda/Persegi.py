def persegi():
    print('==================================')
    print('============= PERSEGI ============')
    print('==================================')
    
    sisi = int(input('sisi\t\t: '))
    luas = lambda s: s * s
    keliling = lambda s: 4 * s

    print('Luas\t\t: ',luas(sisi), 'cm2')
    print('keliling\t: ',keliling(sisi), 'cm')

persegi()
