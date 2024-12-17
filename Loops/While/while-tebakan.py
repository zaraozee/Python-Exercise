angka_rahasia = 8
tebakan = -1

while tebakan != angka_rahasia:
    tebakan = int(input("tebak angka (1-10): "))
    if tebakan < angka_rahasia:
        print("tebakan terlalu rendah!")
    elif tebakan > angka_rahasia:
        print("tebakan terlalu tinggi!")
    
print("selamat! kamu menebak angka yang benar")