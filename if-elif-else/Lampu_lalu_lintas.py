warna1 = 'merah' 
warna2 = 'kuning'
warna3 = 'hijau'

warna_lampu = input("masukkan warna lampu lalu lintas: ").lower()

if warna_lampu == warna1:
    print ("berhenti")
elif warna_lampu == warna2:
    print ("bersiap")
elif warna_lampu == warna3:
    print ("maju")
else:
    print ("warna salah")