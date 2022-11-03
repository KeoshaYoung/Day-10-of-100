myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
tip = float(answer * .20)
groupTip = input("Are you guys going to leave a tip?")
if groupTip == "yes":
    print("Great! The average tip is around 20 percent of the bill. That means you guys will tip", tip, "dollars!")
else:
    print("Come on! Don't be cheap!")
