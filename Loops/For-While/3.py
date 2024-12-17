for a in range(3):
    print(f"for loop ke-{a}")
    b = 0
    while b < 5:
        if b == 3:
            break  #keluar dari while loop ketika b == 3
        if b == 1:
            b += 1
            continue  #lompat ke iterasi while berikutnya ketika b == 1
        print(f"  - while loop index: {b}")
        b += 1
