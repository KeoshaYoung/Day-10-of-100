# Day-10-of-100

👉 Day 10 Challenge

Extend your bill calculator

Add a tip function that adds the total tip to the bill before splitting it equally between the people.

Ask the user for the total bill amount.
Ask what % of tip they will leave to be added to the bill total.
Figure out how to get the total bill with tip then add that to original amount.
Ask the user how many people are splitting the bill and divide by the total.
You can use the same code to get started:

```
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
```
