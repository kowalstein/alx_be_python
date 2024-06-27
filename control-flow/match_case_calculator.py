# This script uses the match case function to create a calculator

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
# user input

match operation: 
    case "+":
        print(f"The result is {(first_num+second_num)}")
    case "-":
        print(f"The result is {(first_num-second_num)}")
    case "*":
        print(f"The result is {(first_num*second_num)}")
    case "/":
        print(f"The result is {(first_num/second_num)}")
