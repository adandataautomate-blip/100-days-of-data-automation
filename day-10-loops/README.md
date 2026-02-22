## Day-10-loops
## What I learned
For loops are great for iterating through collections like inventory lists.

While loops allow continuous user interaction until a condition is met.

Break helps stop loops early when a specific condition is triggered.

Continue lets me skip certain items without stopping the loop.

## The code
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

## Real Business application
In retail automation, inventory checks must be fast and flexible. A for loop can display all items, while a while loop allows managers to search interactively. Break ensures the process stops when a critical item (like "Camera") is found, and continue skips irrelevant items (like "Charger" if it’s discontinued). Recruiters see that I can design automation that balances efficiency with business rules, making inventory management smarter and less error‑prone.

## What I struggled with
I struggled with remembering when to use break versus continue without accidentally skipping important items.

📌 Connect With Me