import sys
from pathlib import Path

#add src folder to path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from my_calc import main_console 
from my_calc import main_gui

print("choose your interface :")
print("1. use python's console")
print("2. use a graphic interface")
mode = int(input("Choose an option (1-2): "))

if mode == 1:
    main_console.console()
elif mode == 2:
    main_gui.gui()
else:
    print("Invalid choice.")
