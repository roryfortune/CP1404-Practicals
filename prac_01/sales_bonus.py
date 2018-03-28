"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
bonus_0 = sales * 0.10
bonus_1 = sales * 0.15
if sales < 0:
    print("Invalid sales value")
else:
    if sales < 1000:
        print("Congratulations, your bonus is ", "$", bonus_0)
    else:
        print("Congratulations, your bonus is ", "$", bonus_1)