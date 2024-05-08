dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7 : 70, 8 : 80, 9 : 90, 10 : 100}

item = 0
print("Key\tValue\tItem")
for key in dictionary:
    item += 1
    print(f"{key}\t{dictionary[key]}\t{item}")