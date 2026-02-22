# in inventory system checking items
inventory = ["laptop", "phone", "tablet", "charger", "headphones", "camera"]

for invention in inventory:

    item = input("Enter item: ")
    print(item)

    if item == "camera":
        break

    if item == "charger":
        continue

print(invention)