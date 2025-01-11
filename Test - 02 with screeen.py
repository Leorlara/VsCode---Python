import tkinter as tk
from tkinter import messagebox

# Options
options = ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]
options_price = [2.5, 3, 2.5, 3, 2.5, 3.5, 2.5]

sizes = ["Medium", "Large", "Xl"]
sizes_price = [0, 1, 1.5]

# Variables to store choices
selected_option = None
selected_size = None
eat_in = None

# main window
root = tk.Tk()
root.title("Order Menu")
root.geometry("300x300")

# functions
def show_type_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select Your Coffee:").pack(pady=10)
    for i, option in enumerate(options):
        tk.Button(root, text=f"{option} - ${options_price[i]:.2f}",
                  command=lambda opt=option, price=options_price[i]: confirm_type(opt, price)).pack(pady=5)

def confirm_type(option, price):
    global selected_option
    selected_option = (option, price)
    if messagebox.askyesno("Confirmation", f"You selected {option}. Proceed?"):
        show_size_screen()

def show_size_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select Your Size:").pack(pady=10)
    for i, size in enumerate(sizes):
        tk.Button(root, text=f"{size} - Additional ${sizes_price[i]:.2f}",
                  command=lambda sz=size, price=sizes_price[i]: confirm_size(sz, price)).pack(pady=5)

def confirm_size(size, price):
    global selected_size
    selected_size = (size, price)
    if messagebox.askyesno("Confirmation", f"You selected {size} size. Proceed?"):
        show_eat_in_screen()

def show_eat_in_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Eat In or Take Away?").pack(pady=10)
    tk.Button(root, text="Eat In", command=lambda: finalize_order("Here")).pack(pady=5)
    tk.Button(root, text="Take Away", command=lambda: finalize_order("Away")).pack(pady=5)

def finalize_order(choice):
    global eat_in
    eat_in = choice

    # Calculate the final price
    final_price = selected_option[1] + selected_size[1] + (1 if eat_in == "Away" else 0)
    messagebox.showinfo("Final Price", f"The total price is: ${final_price:.2f}")

    # Optionally restart or close
    if messagebox.askyesno("Restart?", "Would you like to place another order?"):
        show_type_screen()
    else:
        root.destroy()

# Start with the type screen
show_type_screen()

# Run the application
root.mainloop()