A = int(input("masukan panjang sisi pertama (A): "))
B = int(input("masukan panjang sisi kedua (B): "))
C = int(input("masukan panjang sisi ketiga (C): "))

# memastikan A < B < C
if A > B:
    A, B = B, A
if B > C:
    B, C = C, B
if A > B: 
    A, B = B, A
  
A2 = A ** 2
B2 = B ** 2
C2 = C ** 2

#menemukan jenis segitiga
if A2 + B2 == C2:
    print("segitiga siku-siku")
elif A2 + B2 > C2:
    print("segitiga lancip")
else:
    print("segitiga tumpul")

