
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese= input("Do you want extra cheese? Y or N ")

small_pizza=15
medium=20
large=25
pepperoni_small=2
pepperoni_medium_large=3
extra=1
price=0
if size =="S" and add_pepperoni=="Y" and extra_cheese=="Y":
    price+=small_pizza+pepperoni_small+extra
    print(f"Your final bill is: ${price}.")
elif size =="S" and add_pepperoni=="Y" and extra_cheese=="N":
    price+=small_pizza+pepperoni_small
    print(f"Your final bill is: ${price}.")
elif size =="S" and add_pepperoni=="N" and extra_cheese=="Y":
    price+=small_pizza+extra
    print(f"Your final bill is: ${price}.")
elif size =="S" and add_pepperoni=="N" and extra_cheese=="N":
    price+=small_pizza
    print(f"Your final bill is: ${price}.")

if size =="M" and add_pepperoni=="Y" and extra_cheese=="Y":
    price+=medium+pepperoni_medium_large+extra
    print(f"Your final bill is: ${price}.")
elif size =="M" and add_pepperoni=="Y" and extra_cheese=="N":
    price+=medium+pepperoni_medium_large
    print(f"Your final bill is: ${price}.")
elif size =="M" and add_pepperoni=="N" and extra_cheese=="Y":
    price+=medium+extra
    print(f"Your final bill is: ${price}.")
elif size =="M" and add_pepperoni=="N" and extra_cheese=="N":
    price+=medium
    print(f"Your final bill is: ${price}.")

if size =="L" and add_pepperoni=="Y" and extra_cheese=="Y":
    price+=large+pepperoni_medium_large+extra
    print(f"Your final bill is: ${price}.")
elif size =="L" and add_pepperoni=="Y" and extra_cheese=="N":
    price+=large+pepperoni_medium_large
    print(f"Your final bill is: ${price}.")
elif size =="L" and add_pepperoni=="N" and extra_cheese=="Y":
    price+=large+extra
    print(f"Your final bill is: ${price}.")
elif size =="L" and add_pepperoni=="N" and extra_cheese=="N":
    price+=large
    print(f"Your final bill is: ${price}.")
