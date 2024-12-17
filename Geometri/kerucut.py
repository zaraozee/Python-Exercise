print("="*30)
print('\tRUMUS KERUCUT ')
print("="*30)

PHI = 3.14
r = int(input('masukan jari-jari:'))
s = float(input('masukann sisi kerucut:'))
t = float(input('masukan tinggi kerucut:'))

ls = PHI * r * s 
lp = (PHI * r * s ) + ( PHI * r ** 2 )
v = 1/3 * PHI * r ** 2 * t

print(' luas selimut \t\t: ',ls, "cm")
print( ' luas permukaan \t: ',lp)
print('volume \t\t\t: ',round(v,2))
