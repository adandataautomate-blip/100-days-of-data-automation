# Day-02-variables

## What I learned:
1. Variables help store dynamic values like store IDs and sales.
2.Input data often needs type conversion for numbers.
3.Clear variable names make automation scripts easier to understand.
4.Recruiters value code that scales across multiple stores.

## The code:
# Multiple stores available
multiplestores = [1, 2, 3, 4, 5]

# Ask user for store number
storenum = input("Enter store number: ")
print(storenum)

# Ask user for store ID
storeID = input("Enter store ID: ")
print(f"Store {storenum} has Store ID: {storeID}")

# Ask user for daily sales
dailysales = input("Enter sales amount: ")
print(f"Store {storenum} has daily sales amount: {dailysales}")

# Ask user for transactions
transactions = input("Enter number of transactions: ")
print(f"Store {storenum} has {transactions} transactions")

## Real Business application:
In retail automation, this script can collect daily sales data across multiple stores. Instead of hard‑coding values, variables allow each store manager to enter their store ID, sales, and transactions. This makes the system scalable and adaptable, showing recruiters I can design automation that grows with the business and supports real‑world retail operations.

## What I struggled with:
I struggled with remembering to convert input values into integers or floats so they could be used in calculations later.

📌 Connect With Me:
linkedin.com/in/adan-fatima-automation