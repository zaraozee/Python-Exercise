nilai_uang = int(input("masukan nilai uang: "))

if 100 <= nilai_uang < 1000:
    print("ratusan")
elif 1000 <= nilai_uang < 10000:
    print("ribuan")
elif 10000 <= nilai_uang < 100000:
    print("puluhan ribu")
elif 100000 <= nilai_uang < 1000000:
    print("ratusan ribu")
elif nilai_uang >= 1000000:
    print("jutaan")
else:
    print("di bawah ratusan")
