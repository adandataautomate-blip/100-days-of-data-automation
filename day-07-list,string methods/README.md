## Day-07-list and string methods
## What I learned

Lists store collections of data.

.append() and .remove() manage items.

.sort() organizes workflows.

.count() tracks occurrences.
## The code
# in supply chain, automating tracking shipments
shipment = ["pending", "in transit", "delivered", "cancelled"]

shipment.append("on the way")
print("Current shipments:", shipment)

shipmentstatus = input("Enter shipment status to update: ")

if shipmentstatus == "cancelled":
    shipment.remove("cancelled")

shipment.sort()

delivered_count = shipment.count("delivered")
print("Delivered shipments:", delivered_count)

shipment.append("double order")

print("Updated shipment list:", shipment)

## Real Business application  
In supply chain automation, lists track shipment statuses like pending, in‑transit, and delivered. This helps managers monitor operations and spot delays quickly.

## What I struggled with  
I struggled with extending lists across multiple warehouses.

📌 Connect With Me