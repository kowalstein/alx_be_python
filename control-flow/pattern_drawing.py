# This script print a square pattern

num = int(input("Enter the size of the pattern: "))
# user input
count = num

while count != 0:
    count -= 1
    for i in range (num): 
        print ("*", end='')
    print ()
