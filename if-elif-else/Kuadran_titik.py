x = float(input("masukan nilai x : "))
y = float(input("masukan nilai y : "))

if x > 0 and y > 0:
    kuadran = "kuadran I"
elif x < 0 and y > 0:
    kuadran = "kuadran II"
elif x < 0 and y < 0:
    kuadran = "kuadran III"
elif x > 0 and y < 0:
    kuadran = "kuadran IV"
else:
    print("tidak terletak di kuadran manapun")

print(f"titik P({x}, {y}) terletak di {kuadran}")
