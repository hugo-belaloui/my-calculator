import sys
from pathlib import Path

#add src folder to path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from my_calc import parse_string_operation as pso
from my_calc import priority
from my_calc import history
import tkinter as tk 
from tkinter import messagebox 






        # - INTERFACE TKINTER 


def gui() :
    def press(value):
        entry.insert(tk.END, value)

    def clear():
        entry.delete(0, tk.END)

    def calculate():
        expression = entry.get()
        try:
            parsed = pso.parse_string_calculation(expression)
            result = priority.priority_calculation(parsed)
            clear()
            entry.insert(0, result)
            history.add_to_history(expression, result)
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
        (1, '2', '3', '/'),
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
    tk.Button(root, text="History", width=22, height=2, command=history.load_history).pack(pady=2)
    tk.Button(root, text="Clear History", width=22, height=2, command=history.clear_history).pack(pady=2)

    root.mainloop()