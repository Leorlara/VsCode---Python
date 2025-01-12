import tkinter as tk
from tkinter import messagebox
selected_toppings = []
total_toppings_price = 0

# Options
Container = ["Cup", "Cone"]
Container_price = [0.5, 0.8]

# Toppings
Toppings = ["Flake","Chocolate Sprinkles","Strawberry Coulis"]
Toppings_price = [0.4, 0.3, 0.6]

while True:
    try:
        print(f"Available containers: {', '.join(Container)}")
        Index_Container = Container.index(input("What container would you like? ").strip().title())
        Price_Container = Container_price[Index_Container]
        Confirmation = input("you selected a "+Container[Index_Container]+" for $"+str(Container_price[Index_Container])+" is that correct? (yes/no)").strip().title()
        if Confirmation == "Yes":
            break
    except ValueError:
        print("Sorry, an error occurred. Please try again.")
        


while True:
    try:
        while True:  # Inner loop for selecting multiple toppings
            print(f"Available toppings: {', '.join(Toppings)}")
            user_input = input("What topping would you like? Type 'done' when finished: ").strip().title()
            
            if user_input == "Done":
                break
            
            if user_input in Toppings:  # Valid topping
                Index_Toppings = Toppings.index(user_input)
                Price_Toppings = Toppings_price[Index_Toppings]
                selected_toppings.append(user_input)
                total_toppings_price += Price_Toppings
                print(f"Added {user_input} for ${Price_Toppings:.2f}.")
                Toppings.remove(user_input)
                Toppings_price.remove(Price_Toppings)
                if Toppings == []:
                    print("All toppings have been selected.")
                    break

            else:
                print("Sorry, we don't have that topping option. Please try again.")
        
        break
    except ValueError:
        print("An unexpected error occurred. Please try again.")

# Final result
final_price = Price_Container + total_toppings_price
print("You selected the following toppings:")
print(", ".join(selected_toppings) if selected_toppings else "No toppings")
print(f"Total price for toppings: ${total_toppings_price:.2f}")
print("Final price: $" ,final_price)