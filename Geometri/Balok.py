print('====================================')
print('=============  BALOK ===============')
print('====================================')

panjang = int(input('masukan nilai panjang\t:'))
lebar = int(input('masukan nilai lebar\t:'))
tinggi = int(input('masukan nilai tinggi\t:'))

luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi) 
volume = panjang * lebar * tinggi

print('luas balok\t\t: ',luas, 'cm2')
print('volume balok\t\t:',volume, 'cm3')

