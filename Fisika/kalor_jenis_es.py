print("====================")
print("RUMUS KALOR JENIS ES")
print("====================")

m = int(input("masukan nilai massa :"))
c = int(input("masukan nilai celcius :"))
l = int(input("masukan nilai liter :"))

dt = 0.5
# rumus kalor jenis es
q1 = m * c * dt 
# rumus kalor lebur es
q2 = m * l
# rumus kalor jenis air
q3 = m * c * dt

print("kalor jenis es: ", q1)
print("kalor jenis es: ", q2)
print("kalor jenis es: ", q3)