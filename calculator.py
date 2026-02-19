import re

HISTORY_FILE = "history.txt"
history = []

def add_to_history(operation, result):
    """Adds the operation and result to the history list and file."""
    entry = f"{operation} = {result}"
    history.append(entry)
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{entry}\n")

def convert_int_float(value):
    """Converts a string to int or float if possible."""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def parse_string_calculation(chain):
    """Parses the calculation string into a list of numbers and operators."""
    # Regex to find numbers (including negative) and operators
    # (?<!\d) ensures we don't treat subtraction as a negative number if preceded by a digit
    parsed = re.findall(r'(?<!\d)-?\d+\.?\d*|[-+*/]', chain)
    return [convert_int_float(x) for x in parsed]

def priority_calculation(parsed_chain):
    """Calculates the result of the parsed chain respecting order of operations."""
    if not parsed_chain:
        raise ValueError("Invalid calculation: Empty input")

    # Handle multiplication and division first
    i = 0
    while i < len(parsed_chain):
        if parsed_chain[i] in ['*', '/']:
            # Check for valid operands
            if i == 0 or i == len(parsed_chain) - 1:
                raise ValueError("Invalid operator placement")

            a = parsed_chain[i-1]
            b = parsed_chain[i+1]

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                 raise ValueError(f"Invalid operands for {parsed_chain[i]}")

            if parsed_chain[i] == '*':
                result = a * b
            else:
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = a / b

            parsed_chain[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    # Handle addition and subtraction
    i = 0
    while i < len(parsed_chain):
        if parsed_chain[i] in ['+', '-']:
             # Check for valid operands
            if i == 0 or i == len(parsed_chain) - 1:
                raise ValueError("Invalid operator placement")

            a = parsed_chain[i-1]
            b = parsed_chain[i+1]

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                 raise ValueError(f"Invalid operands for {parsed_chain[i]}")

            if parsed_chain[i] == '+':
                result = a + b
            else:
                result = a - b

            parsed_chain[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    if len(parsed_chain) != 1:
         raise ValueError("Invalid calculation structure")

    return parsed_chain[0]

def main():
    while True:
        print("\n1. Enter your calculation")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit")

        try:
            user_input = input("Choose an option (1-4): ")
            # Handle potential empty input
            if not user_input.strip():
                continue

            if not user_input.strip().isdigit():
                 print("Please enter a valid number.")
                 continue
            choice = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 4:
            break

        if choice == 3:
            history.clear()
            # Truncate the file
            open(HISTORY_FILE, "w").close()
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
                parsed = parse_string_calculation(expression)
                result = priority_calculation(parsed)

                print(f"Result : {expression} = {result}")
                add_to_history(expression, result)

            except (ValueError, ZeroDivisionError) as e:
                print(f"Error: {e}")
            except Exception as e:
                 print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
