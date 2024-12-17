siswa = int(input("masukan nilai siswa :"))

if int(siswa) >= 100:
    print("nilai A")
elif int(siswa) >= 90:
    print("nilai B")
elif int(siswa) >= 80:
    print("nilai C")
elif int(siswa) >= 70:
    print("nilai D")

else:
    print("siswa dinyatakan tidak lulus")