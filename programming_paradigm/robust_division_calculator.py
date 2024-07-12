""" This script implements a division calculator that robustly handles
    errors like division by zero and non-metric inputs."""

def safe_divide(numerator, denominator):
    try:
        numerator/denominator
    except ZeroDivisionError:
        print ('Error: Cannot divide by zero.')
    else:
        pass
    try:
        float(numerator)/float(denominator)
    except ValueError:
        print ('Error: Please enter numeric values only.')
    else:
        print (f"The result of the division is {(numerator/denominator)}")
    return
