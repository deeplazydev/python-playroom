def calculate_finances(monthly_income: float, tax_rate: float, currency_symbol: str) -> None:
    monthly_tax: float = monthly_income * tax_rate / 100
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    print("------------------------------------")
    print(f"Monthly income: {currency_symbol}{monthly_income:,.2f}")
    print(f"Tax rate: {tax_rate:.0f}%")
    print(f"Monthly tax: {currency_symbol}{monthly_tax:,.2f}")
    print(f"Monthly net income: {currency_symbol}{monthly_net_income:,.2f}")
    print(f"Yearly salary: {currency_symbol}{yearly_salary:,.2f}")
    print(f"Yearly tax paid: {currency_symbol}{yearly_tax:,.2f}")
    print(f"Yearly net income: {currency_symbol}{yearly_net_income:,.2f}")
    print("------------------------------------")


def main() -> None:
    monthly_input: float = float(input("Enter your monthly salary: "))
    tax_rate: float = float(input("Enter your tax rate (%): "))

    calculate_finances(monthly_input, tax_rate, currency_symbol="$")


if __name__ == "__main__":
    main()


"""
Homework:
1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships)
so they can see how much they have left over the month.
2. Recreate the user input section to safely handle users inserting the wrong type without
crashing the program.
"""
