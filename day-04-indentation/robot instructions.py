# In logistics company, automating robot instructions
robotactions = ["scanning the item barcode" , "logging the scan into the central database" , "moving the item to the assigned shelf" , "confirming placement with a sensor check"]
for robotactin in robotactions:
    if robotactin is False:
        print("error")
    print("My action is" , robotactin)
