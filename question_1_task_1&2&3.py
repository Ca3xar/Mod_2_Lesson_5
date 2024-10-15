operator = input("enter an operator (* / + -): ")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))


if operator == "*":
    result = num1 * num2
    print(round(result,  5))
elif operator == "/":
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = 0
    print(round(result,  5))  
elif operator == "+":
    result = num1 + num2
    print(round(result,  5))
elif operator == "-":
    result = num1 - num2
    print(round(result,  5))
else:
    print(f"{operator} is not valid")