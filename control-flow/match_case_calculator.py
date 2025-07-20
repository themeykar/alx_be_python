num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        if operation == '+':
            result = num1 + num2
            print(f"The result is {result}. ")
    case '-':
        if operation == '-':
            result = num1 - num2
            print(f"The result is {result}. ")

    case '*':
        if operation == '*':
            result = num1 * num2
            print(f"The result is {result}. ")

    case '/':
        if operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}. ")

            elif num2 == 0:
                print("Cannot divide by zero.")

