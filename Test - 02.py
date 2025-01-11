#Types
Options = ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]
Options_Price = [2.5, 3, 2.5, 3, 2.5, 3.5, 2.5]

while True:
    try:
        Index_type = Options.index(input("What would you like to order? "))
        Price_Type= Options_Price[Index_type]
        break
    except ValueError:
        print("Sorry, we don't have that option or a typo was made. Please try again.")

#Sizes
Sizes = ["Medium", "Large", "Xl"]
Sizes_Price = [0, 1, 1.5]\

while True:
    try:
        Index_Size= Sizes.index(input("What size would you like? "))
        Price_Size= Sizes_Price[Index_Size]
        break
    except ValueError:
        print("Sorry, we don't have that option or a typo was made. Please try again.")

#Eat nt or take away
while True:
    Eat = (input("Would you like to eat in or take away? Here/Away "))
    if Eat == "Here" or Eat == "Away":
        break
    else:
        print("Sorry, we don't have that option or a typo was made. Please try again.")

#Final Price
if Eat == "Away":
    Final_price = Price_Type+Price_Size+1
else:
    Final_price = Price_Type+Price_Size

print("The final price is: ", Final_price)
