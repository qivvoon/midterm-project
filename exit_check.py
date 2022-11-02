from log import usual_log

def next_calculation_check():
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            usual_log.error("Let's do next calculation? => no")
            return one_more_check()

        elif next_calculation.lower() == "yes":
            usual_log.error("Let's do next calculation? => yes")
            return "continue"

        else:
            usual_log.error("Let's do next calculation? => " + next_calculation)
            continue


def one_more_check():
    while True:
        one_more_check = input("Are you sure? (yes/no): ")
        if one_more_check.lower() == "yes":
            usual_log.error("Are you sure? => yes")
            return "break"

        elif one_more_check.lower() == "no":
            usual_log.error("Are you sure? => no")
            return "continue"

        else:
            usual_log.error("Are you sure? => " + one_more_check)
            continue