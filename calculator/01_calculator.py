print("Calculator")

a = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Answer:", a + b)

elif op == "-":
    print("Answer:", a - b)

elif op == "*":
    print("Answer:", a * b)

elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Answer:", a / b)

else:
    print("Invalid operation")
