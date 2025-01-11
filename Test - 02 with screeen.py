import tkinter as tk
from tkinter import messagebox

# Options and prices
options = ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]
options_price = [2.5, 3, 2.5, 3, 2.5, 3.5, 2.5]

sizes = ["Medium", "Large", "Xl"]
sizes_price = [0, 1, 1.5]

# Global variables to store user selections
selected_option = None
selected_size = None
eat_in = None

def select_option(option, price):
    global selected_option
    selected_option = (option, price)
    messagebox.showinfo("Selection", f"You selected {option} - ${price:.2f}")

def select_size(size, price):
    global selected_size
    selected_size = (size, price)
    messagebox.showinfo("Selection", f"You selected {size} size - Additional ${price:.2f}")

def select_eat_in(choice):
    global eat_in
    eat_in = choice
    messagebox.showinfo("Selection", f"You selected to {'eat in' if choice == 'Here' else 'take away'}.")

def calculate_price():
    if not selected_option or not selected_size or not eat_in:
        messagebox.showwarning("Incomplete Order", "Please complete your selection before proceeding.")
        return
    
    final_price = selected_option[1] + selected_size[1] + (1 if eat_in == "Away" else 0)
    messagebox.showinfo("Final Price", f"The total price is: ${final_price:.2f}")

# Create the main window
root = tk.Tk()
root.title("Order Menu")

# Create buttons for coffee options
tk.Label(root, text="Select Your Coffee:").pack()
for i, option in enumerate(options):
    tk.Button(root, text=f"{option} - ${options_price[i]:.2f}",
              command=lambda opt=option, price=options_price[i]: select_option(opt, price)).pack(pady=2)

# Create buttons for sizes
tk.Label(root, text="Select Your Size:").pack()
for i, size in enumerate(sizes):
    tk.Button(root, text=f"{size} - Additional ${sizes_price[i]:.2f}",
              command=lambda s=size, price=sizes_price[i]: select_size(s, price)).pack(pady=2)

# Create buttons for eat-in/takeaway
tk.Label(root, text="Eat In or Take Away:").pack()
tk.Button(root, text="Here", command=lambda: select_eat_in("Here")).pack(pady=2)
tk.Button(root, text="Away", command=lambda: select_eat_in("Away")).pack(pady=2)

# Finalize order button
tk.Button(root, text="Calculate Final Price", command=calculate_price).pack(pady=10)

# Run the GUI
root.mainloop()