def main():
    """
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
    """


def main():
    sales = float(input("Enter Sales: $"))
    while sales <= 0:
        print("invalid")
        sales = float(input("Enter Sales: $"))
    if sales < 1000:
        bonus_calc = ten_percent_calc(sales)
    else:
        bonus_calc = fifteen_percent_calc(sales)

    print("Sale made $", sales, "Bonus from sale $", bonus_calc)


def fifteen_percent_calc(sales):
    bonus_calc = sales * 0.15
    return bonus_calc


def ten_percent_calc(sales):
    bonus_calc = sales * 0.1
    return bonus_calc


main()
