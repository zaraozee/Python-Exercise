x = int(input("Masukkan jarak yang ditempuh : "))

#km = 100000
#m = 100

km = x // 100000
sisa_cm = x % 100000
m = sisa_cm // 100
cm = sisa_cm % 100

print(f"Jarak yang ditempuh adalah: {km}km  {m}m  {cm}cm")
