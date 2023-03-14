num1 = float(input("Wprowadz pierwsą liczbę: "))
num2 = float(input("Wprowadz drugą liczbę: "))
operation = input("Wprowadz operacje: ")

print(f"{num1} {operation} {num2} =", end = " ")

match operation:
    case "+":
        print((num1+num2))

    case "-":
        print((num1-num2))

    case "*":
        print((num1*num2))

    case "/":
        print((num1/num2))

    case "^":
        print((num1**num2))

    case _:
        print("Wrong operation")