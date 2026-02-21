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