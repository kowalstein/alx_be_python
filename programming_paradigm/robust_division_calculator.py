""" This script implements a division calculator that robustly handles
    errors like division by zero and non-metric inputs."""

def safe_divide(numerator, denominator):
    try:
        numerator/denominator
    except ZeroDivisionError:
        return ('Error: Cannot divide by zero.')
    else:
        pass
    try:
        float(numerator)/float(denominator)
    except ValueError:
        return ('Error: Please enter numeric values only.')
    else:
        pass 
    return (f"The result of the division is {(numerator/denominator)}")