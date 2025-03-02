from collections.abc import Callable


def format_currency(amount: float, currency_symbol: str) -> str:
    """
    Convert amount into a formatted string
    Format: SYMBOL+VALUE (comma for thousands, point for decimal separator, two decimals)
    """
    return f"{currency_symbol}{amount:,.2f}"


def dollar_money_formatter(amount: float) -> str:
    """
    Format amount into a string representation using dollar as unit
    :param amount: value
    :return: $value
    """
    return format_currency(amount, "$")


def read_float_value(message: str) -> float:
    """
    Read valid float value.
    The function will ask multiple times until the user enters a valid float number.
    """
    while True:
        try:
            data = input(message)
            value: float = float(data)
            return value

        except ValueError:
            print("The value is not a valid numeric value, please enter it again.\n")


def read_expenses() -> dict:
    expenses: dict = {}

    while True:
        category: str = input("Give the category name of the expenses ('none' for finish): ")
        if not category:
            continue
        elif category.lower() == "none":
            break

        expenses[category] = read_float_value(f"Enter the amount in expense '{category}': ")

    return expenses


def calculate_finances(monthly_income: float, tax_rate: float, expenses: dict, currency_formatter: Callable) -> None:
    monthly_tax: float = monthly_income * tax_rate / 100
    monthly_expenses: float = sum(expenses.values())
    monthly_net_income: float = monthly_income - monthly_tax - monthly_expenses
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_expenses: float = monthly_expenses * 12
    yearly_net_income: float = yearly_salary - yearly_tax - yearly_expenses

    print("--------------------------------------------")
    print(f"Monthly income: {currency_formatter(monthly_income)}")
    print(f"Tax rate: {tax_rate:.0f}%")
    print(f"Monthly tax: {currency_formatter(monthly_tax)}")
    for key in expenses.keys():
        print(f"Monthly expenses on {key}: {currency_formatter(expenses[key])}")
    print(f"Monthly net income: {currency_formatter(monthly_net_income)}")

    print(f"Yearly salary: {currency_formatter(yearly_salary)}")
    print(f"Yearly tax paid: {currency_formatter(yearly_tax)}")
    print(f"Yearly expenses: {currency_formatter(yearly_expenses)}")
    print(f"Yearly net income: {currency_formatter(yearly_net_income)}")
    print("--------------------------------------------")


def main() -> None:
    """
    Ask user for data and present the financial results.
    """
    monthly_input: float = read_float_value("Enter your monthly salary: ")
    tax_rate: float = read_float_value("Enter your tax rate (%): ")
    expenses: dict = read_expenses()

    calculate_finances(monthly_input, tax_rate, expenses, dollar_money_formatter)


def main_example() -> None:
    """
    Example with some values
    """
    monthly_input: float = 5100
    tax_rate: float = 43
    expenses: dict = {"tango": 45, "super": 200, "rent": 650, "services": 110, "hollidays": 120}

    calculate_finances(monthly_input, tax_rate, expenses, dollar_money_formatter)


if __name__ == "__main__":
    #main_example()
    main()

