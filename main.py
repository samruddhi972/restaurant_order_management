print("Welcome to Sam Restaurant!\n")
print("MENU\n")


items = {
    'pizza': 40,
    'burger': 30,
    'samosa': 10,
    'cocktail': 30,
    'coffee': 20
}


for item, price in items.items():
    print(f"{item.capitalize()}: ₹{price}")

print("\nPlease place your order below:")

order_total = 0


while True:
    item = input("\nEnter the name of the item you want to order: ").lower()

    if item in items:
        order_total += items[item]
        print(f" Your item '{item}' is added to your order.")
    else:
        print(f" Sorry, '{item}' is not available.")

    another = input("Do you want to order another item? (yes/no): ").lower()
    if another != "yes":
        break

print(f"\n Your total bill is: ₹{order_total}")
print(" Thank you for ordering from Sam Restaurant!")
