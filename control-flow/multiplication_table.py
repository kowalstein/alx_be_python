# This script prints the multiplication table for any user inputed number

number = int(input("Enter a number to see its multiplication table: "))
#user input

for i in range (1,11):
    print(f"{number} * {i} = {number*i}")
