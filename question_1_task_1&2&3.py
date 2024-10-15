def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "x" + "/" + "y"
    return x / y
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def calculator():
    print("1. multiply")
    print("2. divide")
    print("3. add")
    print("4. subtract")
    print("5. quit")
    while True:
        operation = input("enter operator: ")
            
        if operation.lower() == '5':
                print("Farewell...")
                break
        if operation in ("1","2","3","4"):
                try:
                    x = float(input("enter the first number: "))
                    y = float(input("enter the second number: "))
                except ValueError:
                    print("invalid input")
                    continue
                    
                if operation == "1":
                    print(f"{x} * {y}")
                elif operation == "2":
                    print(f"{x} / {y}")
                elif operation == "3":
                    print(f"{x} + {y}")
                elif operation == "4":
                    print(f"{x} - {y}")
        else:
            print("invalid operation")
if __name__ == "__main__":
    calculator()