history = []

def add_to_history(operation, result):
    history.append(f"{operation} = {result}")
    with open("history.txt", "a") as folder:
        folder.write(f"{operation} = {result}\n")