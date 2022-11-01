import calc_function.calc_add as calc_add 
import calc_function.calc_sub as calc_sub 
import calc_function.calc_mul as calc_mul
import calc_function.calc_div as calc_div


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
            print(num1, "+", num2, "=", calc_add.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", calc_sub.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", calc_mul.multiply(num1, num2))
            
        elif choice =='4':
            if num2 == 0:
                print("error! can't divide by zero")
            else:
                print(num1, "/", num2, "=", calc_div.divide(num1,num2))


        state_check = "break"
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")

            if next_calculation.lower() == "no":
                one_more_check = input("Are you sure? (yes/no): ")
                if one_more_check.lower() == "yes":
                    break
                elif one_more_check.lower() == "no":
                    state_check = "continue"
                    break

            elif next_calculation.lower() == "yes":
                state_check = "continue"
                break

        if state_check == "break":
            break

        elif state_check == "continue":
            continue


    else:
        print("Invalid Input")