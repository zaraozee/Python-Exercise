counter = 0
while counter < 3:
    print(f"Iterasi while ke-{counter}")
    for i in range(5):
        print(f"  - for loop index: {i}")
    
    counter += 1
