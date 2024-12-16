print("\tHITUNG BULAN PERNIKAHAN")
print("---------------------------------------")

current_month = int(input("Masukkan bulan saat ini (1-12): "))
months_ahead = int(input("Masukkan berapa bulan ke depan: "))

wedding_month = (current_month + months_ahead) % 12

#jika hasilnya 0, artinya bulan pernikahan adalah Desember (12)
if wedding_month == 0:
    wedding_month = 12

print(f"Bulan pernikahan adalah bulan ke-{wedding_month}")
