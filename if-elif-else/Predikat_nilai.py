predikat_nilai = int(input('masukan nilai : '))

if predikat_nilai >= 90 and predikat_nilai <= 100:
    print('A')
elif predikat_nilai >= 80 and predikat_nilai <= 89:
    print('b')
elif predikat_nilai >= 70 and predikat_nilai <= 79:
    print('c')
elif predikat_nilai >= 60 and predikat_nilai <= 69:
    print('d')
elif predikat_nilai < 60:
    print('e')

else:
  print('selain itu nilai salah') 