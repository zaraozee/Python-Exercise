print("============================")
print("\tLAMA BEKERJA")
print("============================")

jam_masuk = int(input("Masukkan jam masuk (1-12): "))
jam_pulang = int(input("Masukkan jam pulang (1-12): "))

if jam_masuk <= jam_pulang:
    lama_bekerja = jam_pulang - jam_masuk
else:
    lama_bekerja = (12 - jam_masuk) + jam_pulang

print("\n--- Lama Bekerja ---")
print(f"Lama bekerja: {lama_bekerja} jam")
