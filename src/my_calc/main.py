import re
from . import intfloat as cif
from . import parse_string_operation as pso
from . import priority


# history

history = []

def add_to_history(operation, result):
    history.append(f"{operation} = {result}")
    with open("history.txt", "a") as folder:
        folder.write(f"{operation} = {result}\n")


# calcul

cif.convert_int_float


pso.parse_string_calculation

priority.priority_calculation


# menu

while True:
    print("\n1. Enter your calculation")
    print("2. View history")
    print("3. Clear history")
    print("4. Exit")

    try:
        choice = int(input("Choose an option (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 4:
        break

    if choice == 3:
        history.clear()
        open("history.txt", "w").close()
        print("History cleared.")
        continue

    if choice == 2:
        print("\nHistory:")
        if not history:
            print("No operations yet.")
        else:
            for h in history:
                print(h)
        continue

    if choice == 1:
        expression = input("Enter your calculation : ")

        try:
            parsed = pso.parse_string_calculation(expression)
            result = priority.priority_calculation(parsed)

            print(f"Result : {expression} = {result}")
            add_to_history(expression, result)

        except ValueError:
            print("Invalid expression.")

