a = int(input("masukan bilangan pertama: "))
b = int(input("masukan bilangan kedua: "))
c = int(input("masukan bilangan ketiga: "))

if a > b:
    a,b = b,a
if b > c:
    b,c = c,b
if a > b:
    a,b = b,a

print("bilangan yang terurut adalah: ",a,b,c)