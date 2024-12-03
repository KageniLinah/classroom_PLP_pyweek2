
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

if op == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == '/' and num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid input or division by zero.")
