""" This script defines a function that performs basic arithmetic operations."""

def perform_operation(num1,num2,operation):
    match operation:
        case 'add':
            result = float(num1)+float(num2)
        case 'subtract':
            result = float(num1)-float(num2)
        case 'multiply':
            result = float(num1)*float(num2)
        case 'divide':
            result = float(num1)/float(num2)
    return result
