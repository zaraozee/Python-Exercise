#contoh 1
for a in range(1,6):
    for b in range(1,a + 1):
        print('*', end=' ')
    print()

#contoh 2
huruf = ("*", "**", "***", "****", "*****")
for a in range(5):
    print(huruf[a])

#contoh 3
for a in range (5 + 1):
    print("* " * a)