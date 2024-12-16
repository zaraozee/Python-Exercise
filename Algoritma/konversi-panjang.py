panjang_meter = float(input("Masukkan panjang benda dalam meter: "))

inchi_per_meter = 39.3701  # 1 meter = 39.3701 inch
kaki_per_meter = 3.28084   # 1 meter = 3.28084 feet
yard_per_meter = 1.09361   # 1 meter = 1.09361 yard

# Mengonversi panjang ke dalam satuan inchi, kaki, dan yard
panjang_inchi = panjang_meter * inchi_per_meter
panjang_kaki = panjang_meter * kaki_per_meter
panjang_yard = panjang_meter * yard_per_meter

print(f"Panjang dalam inchi: {panjang_inchi:.2f} inchi")
print(f"Panjang dalam kaki: {panjang_kaki:.2f} kaki")
print(f"Panjang dalam yard: {panjang_yard:.2f} yard")
