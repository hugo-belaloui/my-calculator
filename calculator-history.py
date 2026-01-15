
history = []

def add_to_history(operation, result):
    history.append(f"{operation} = {result}")
    folder = open("history.txt" , "a")
    folder.write(f" {operation} = {result}\n")
    folder.close


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error : cannot divide by 0. "
    return a / b


while True:
    print("\n1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. View history")
    print("6. Clear history")
    print("7. Exit")

    menu = int(input("Choose an option (1-7) : "))
    
    if menu not in range (1, 8) :
        print("\nplease choose a number between 1 and 7 ")
        continue
    else:
        choice = menu
        
        if choice == 7 :
            break


        if choice == 6 :
            folder = open("history.txt" , "w")
            folder.close
            continue

        if choice == 5 :
            print("\nHistory")
            if not history:
                print("\nno operation .")
            else:
                for calcul in history:
                    print(f"\n{calcul}")
            continue

        try:
            num1 = float(input("Enter your first number : "))
            num2 = float(input("Enter your second number : "))
        except ValueError:
            print("Error : enter valid numbers.")
            continue


        if choice == 1 :
            result = add(num1, num2)
            operation = (f"{num1} + {num2}")
        elif choice == 2 :
            result = subtract(num1, num2)
            operation = (f"{num1} - {num2}")
        elif choice == 3 :
            result = multiply(num1, num2)
            operation = (f"{num1} * {num2}")
        elif choice == 4 :
            result = divide(num1, num2)
            operation = (f"{num1} / {num2}")

        else:
            print("error")
            continue

        print(f"Result : {operation} = {result}")

        
        add_to_history(operation, result)
