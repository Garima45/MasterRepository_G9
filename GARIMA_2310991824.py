import tkinter as tk
import math

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_exponential():
    try:
        result = math.exp(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_log():
    try:
        result = math.log(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_pi():
    entry.insert(tk.END, math.pi)

def calculate_percentage():
    try:
        result = eval(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Colored Calculator")

# Entry widget for input and display
entry = tk.Entry(root, width=20, font=('Arial', 14), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=6)

# Button colors
button_color = "#d9d9d9"  # Light gray
operator_color = "#FFA500"  # Orange

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'exp', 'sqrt', 'log', 'π', '%'
]

row_val = 1
col_val = 0

for button in buttons:
    if button in {'=', 'exp', 'sqrt', 'log', 'π', '%'}:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), bg=operator_color,
                  command=calculate_exponential if button == 'exp' else
                          calculate_square_root if button == 'sqrt' else
                          calculate_log if button == 'log' else
                          insert_pi if button == 'π' else
                          calculate_percentage if button == '%' else
                          calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), bg=button_color,
                  command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 5:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 14), bg=operator_color, command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

# Run the GUI
root.mainloop()
