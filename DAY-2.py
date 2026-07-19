print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? :$"))
tip = int(input("What percentage tip would you like to give?: "))
tip_amt = bill * (tip / 100)
print(f"The tip amount is :${round(tip_amt , 4)}")
total = bill + tip_amt
people = int(input("How many people to split the bill?: "))
final_total = total / people
print(f"Each person should pay $ {round(final_total , 4)}")
