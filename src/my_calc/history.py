history = []

# add the result to the history 
def add_to_history(operation, result):
    history.append(f"{operation} = {result}")
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"{operation} = {result}\n")

#clear the history
def clear_history():
    history.clear()
    open("history.txt", "w").close()

#show the history
def load_history():
    history.clear()
    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            for line in f:
                history.append(line.strip())
    except FileNotFoundError:
        pass
