def main():
    print("Welcome to MY Restaurant!\n")

    
    time = input("What time is it? (e.g., 7:30 a.m. or 13:00): ")
    time_float = convert(time)

    if 7.0 <= time_float <= 8.0:
        print("It's breakfast time \n")
    elif 12.0 <= time_float <= 13.0:
        print("It's lunch time \n")
    elif 18.0 <= time_float <= 19.0:
        print("It's dinner time \n")
    else:
        print("We're open all day! \n")

    #  menu
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
            print(f"Your item '{item}' is added to your order.")
        else:
            print(f"Sorry, '{item}' is not available.")

        another = input("Do you want to order another item? (yes/no): ").lower()
        if another != "yes":
            break

    print(f"\nYour total bill is: ₹{order_total}")

    # Checkout
    print("\n----- Checkout -----")
    print("Select your payment method:")
    print("1. UPI")
    print("2. Cash")
    print("3. Card")

    while True:
        payment = input("Enter your choice (1/2/3): ")

        if payment == "1":
            print("You selected UPI. Please scan the QR code to complete your payment. ")
            break
        elif payment == "2":
            print("You selected Cash. Please pay the amount at the counter. ")
            break
        elif payment == "3":
            print("You selected Card. Please insert your card and enter your PIN. ")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nThank you for ordering from MY Restaurant! Have a great day! ")


def convert(time):
    time = time.strip().lower()

    if "a.m." in time or "p.m." in time:
        time, period = time.split()
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        if period == "p.m." and hours != 12:
            hours += 12
        elif period == "a.m." and hours == 12:
            hours = 0
    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

    return hours + minutes / 60


if __name__ == "__main__":
    main()
