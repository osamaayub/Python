num1 = float(input("Enter first number:"))
num2 = float(input("Enter Second number:"))
operation = (input("Enter an operation:"))
result = 0
print("+ for Addition:")
print("- for Subtraction:")
print("/ for Division")
print("* for Multiplication")
if operation == '+':
    result = num1+num2
    print(result)
elif operation == '-':
    result = num1-num2
    print(result)
elif operation == '/':
    result = num1/num2
    print(result)
else:
    result = num1*num2
    print(result)
