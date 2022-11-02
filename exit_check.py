def next_calculation_check():
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            return one_more_check()

        elif next_calculation.lower() == "yes":
            return "continue"

        else:
            continue


def one_more_check():
    while True:
        one_more_check = input("Are you sure? (yes/no): ")
        if one_more_check.lower() == "yes":
            return "break"

        elif one_more_check.lower() == "no":
            return "continue"

        else:
            continue