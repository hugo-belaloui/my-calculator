import re
import tkinter as tk 
from tkinter import messagebox 



# - HISTORIQUE 

history = []

def add_to_history(operation, result):
    history.append(f"{operation} = {result}")
    with open("history.txt", "a") as folder:
        folder.write(f"{operation} = {result}\n")

def clear_history():
    history.clear()
    open("history.txt", "w").close()
    messagebox.showinfo("History", "History cleared.")

def show_history():
    if not history:
        messagebox.showinfo("History", "No operations yet.")
    else:
        messagebox.showinfo("History", "\n".join(history))




# - CALCUL AVEC PRIORITÉ 

def convert_int_float(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def parse_string_calculation(chain):
    parsed = re.findall(r'(?<!\d)-?\d+\.?\d*|[-+*/]', chain)
    return [convert_int_float(x) for x in parsed]

def priority_calculation(parsed_chain):
    i = 0
    while i < len(parsed_chain):
        if parsed_chain[i] in ['*', '/']:
            a = parsed_chain[i-1]
            b = parsed_chain[i+1]

            if parsed_chain[i] == '*':
                result = a * b
            else:
                if b == 0:
                    return "Error"
                result = a / b

            parsed_chain[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    i = 0
    while i < len(parsed_chain):
        if parsed_chain[i] in ['+', '-']:
            a = parsed_chain[i-1]
            b = parsed_chain[i+1]

            if parsed_chain[i] == '+':
                result = a + b
            else:
                result = a - b

            parsed_chain[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    return parsed_chain[0]





# - INTERFACE TKINTER 

def press(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        parsed = parse_string_calculation(expression)
        result = priority_calculation(parsed)
        clear()
        entry.insert(0, result)
        add_to_history(expression, result)
    except:
        clear()
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculatrice")
root.geometry("260x480")
root.resizable(False, False)

#ecran
entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(fill="x", padx=10, pady=10)

buttons = [
    ('1', '2', '3', '/'),
    ('4', '5', '6', '*'),
    ('7', '8', '9', '-'),
    ('0', '.', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for btn in row:
        action = calculate if btn == '=' else lambda x=btn: press(x)
        tk.Button(
            row_frame,
            text=btn,
            width=5,
            height=2,
            font=("Arial", 14),
            command=action
        ).pack(side="left", padx=3, pady=3)

tk.Button(root, text="C", width=22, height=2, command=clear).pack(pady=4)
tk.Button(root, text="History", width=22, height=2, command=show_history).pack(pady=2)
tk.Button(root, text="Clear History", width=22, height=2, command=clear_history).pack(pady=2)

root.mainloop()

