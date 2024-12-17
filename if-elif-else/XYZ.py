x = int(input("Masukan nilai x: "))
y = int(input("Masukan nilai y: "))
z = int(input("Masukan nilai z: "))

if x >= y >= z:
    print ("nilai X adalah yang paling besar dan Z nilai terkecil")
elif x >= z >= y:
    print ("nilai X adalah yang paling besar dan Y nilai terkecil")
elif y >= x >=z:
    print ("nilai Y adalah yang paling besar dan Z nilai terkecil ")
elif y >= z >=x:
    print ("nilai Y adalah yang paling besar dan X nilai terkecil ")
elif z >= x >=y:
    print ("nilai Z adalah yang paling besar dan Y nilai terkecil ")
elif z >= y >=x:
    print ("nilai Z adalah yang paling besar dan X nilai terkecil ")