import sys
from pathlib import Path

#add src folder to path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from my_calc import parse_string_operation as pso
from my_calc import priority
from my_calc import history

def console():
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
            history.clear_history()
            open("history.txt", "w").close()
            print("History cleared.")
            continue

        if choice == 2:
            print("\nHistory:")
            if not history.history:
                print("No operations yet.")
            else:
                for h in history.history:
                    print(h)
            continue

        if choice == 1:

            expression = (input("Enter your operation : ")) #input the equation and parse it by calling the adequate function
            try:
                parsed = pso.parse_string_calculation(expression)
                result = priority.priority_calculation(parsed)
                    
                print(f"Result : {expression} = {result}")
                history.add_to_history(expression, result)


            except (IndexError, ValueError, TypeError): #dealing with errors
                print("Erreur : incorrect equation (ex: operator without number)")