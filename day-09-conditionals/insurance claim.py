# In healthcare, automating patient insurance claims
amount = int(input("Enter patient claim amount: "))
insurancestatus = "inactive"
if insurancestatus == "inactive":
    print("auto reject")
elif amount > 50000:
    print("manual review")
else:
    print("send to compliance team")

