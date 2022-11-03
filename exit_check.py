from log import usual_log

# 프로그램을 종료할 것이라면 "break"를, 계속 진행할 것이라면 "continue"를 return한다.
# "yes" 또는 "no" 입력 시 대소문자도 허용해주기 위해 lower()을 사용하였다.
# "yes" 또는 "no"가 아닌 다른 입력을 했을 시, 다시 질문한다.  
def next_calculation_check():
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            usual_log.error("Let's do next calculation? => " + next_calculation)
            return one_more_check()

        elif next_calculation.lower() == "yes":
            usual_log.error("Let's do next calculation? => " + next_calculation)
            return "continue"

        else:
            usual_log.error("Let's do next calculation? => " + next_calculation)
            continue

# "Let's do next calculation?" 질문에 "no"를 답하였을 때, 종료를 재확인 하기 위해 실행되는 함수이다.
# 프로그램을 종료할 것이라면 "break"를, 계속 진행할 것이라면 "continue"를 return한다.
# "yes" 또는 "no" 입력 시 대소문자도 허용해주기 위해 lower()을 사용하였다.
# "yes" 또는 "no"가 아닌 다른 입력을 했을 시, 다시 질문한다.
def one_more_check():
    while True:
        one_more_check = input("Are you sure? (yes/no): ")
        if one_more_check.lower() == "yes":
            usual_log.error("Are you sure? => " + one_more_check)
            return "break"

        elif one_more_check.lower() == "no":
            usual_log.error("Are you sure? => " + one_more_check)
            return "continue"

        else:
            usual_log.error("Are you sure? => " + one_more_check)
            continue