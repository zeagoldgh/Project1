print("""WELCOME TO MY SHOP!""")

item   = input("What item are you purchasing? ")
price  = input("What is the price of " + item + "?" + " ")
amount = input("How many" + item + " " + "are you buying? ")


total = str(int(amount) * float(price))

print("Added " + amount + " " + item + "(s) to shopping cart")
print("Subtotal: $" + total)