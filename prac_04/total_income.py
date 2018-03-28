def main():
    incomes = []
    no_of_months = int(input("Number of months? "))

    for month in range(1, no_of_months + 1):
        income = float(
            input("Please enter income for the month {}: ".format(month)))
        incomes.append(income)

    income_report(incomes)

def income_report(incomes):
    print("Income for month(s): ")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))

main()
