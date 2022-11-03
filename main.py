import calc_function.calc_add as calc_add 
import calc_function.calc_sub as calc_sub 
import calc_function.calc_mul as calc_mul
import calc_function.calc_div as calc_div
from exit_check import next_calculation_check
from log import usual_log
from log import unusual_log

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            usual_log.error(str(num1)+ " + " + str(num2))
            print(num1, "+", num2, "=", calc_add.add(num1, num2))

        elif choice == '2':
            usual_log.error(str(num1)+ " - " + str(num2))
            print(num1, "-", num2, "=", calc_sub.subtract(num1, num2))

        elif choice == '3':
            usual_log.error(str(num1)+ " * " + str(num2))
            print(num1, "*", num2, "=", calc_mul.multiply(num1, num2))
            
        elif choice =='4':
            if num2 == 0:
                unusual_log.error("divide by zero")
                print("error! can't divide by zero")
            else:
                usual_log.error(str(num1)+ " / " + str(num2))
                print(num1, "/", num2, "=", calc_div.divide(num1,num2))

        # next_calculation_check() 실행 후 return된 값이 
        # "break"라면 프로그램을 종료하고,
        # "continue"라면 프로그램을 계속 진행한다.
        state_check = next_calculation_check()

        if state_check == "break":
            break

        elif state_check == "continue":
            continue

    else:
        unusual_log.error("another choice selected")
        print("Invalid Input")