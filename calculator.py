import tkinter as tk

# Functions
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Window
root = tk.Tk()
root.title("Calculator App")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.pack(pady=10)

# Buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    action = lambda x=button: click(x) if x != '=' else equal()
    tk.Button(frame, text=button, width=5, height=2, command=action).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="Clear", command=clear).pack(pady=10)

root.mainloop()