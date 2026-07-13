num1 = int(input('Enter A number='))
num2 = int(input('Enter B number='))

operator = input("Enter operator (+, -, *, /): ")


if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:  # zero division check
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero not allowed!")
else:
    print("Error: Invalid operator entered!")
