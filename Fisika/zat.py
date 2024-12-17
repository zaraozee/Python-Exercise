suhu = float(input("masukkan suhu zat: "))

if suhu <= 0:
    keadaan_zat = "padat"
elif 0 < suhu < 100:
    keadaan_zat = "cair"
else:
    keadaan_zat = "gas"

print(f"\nPada suhu {suhu}°C, zat tersebut berada dalam keadaan {keadaan_zat}.")