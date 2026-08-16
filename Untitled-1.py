while True:
    user_input = input("Are you ready to check in? (Type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    height = int(input("Enter your height in cm: "))
    has_ticket = input("Do you have a ticket? (yes/no): ").lower()

    if height >= 120 and has_ticket == 'yes':
        print("You can ride the roller coaster! Enjoy!")
    elif height < 120:
        print("Sorry, you are too short to ride.")
    else:
        print("You need a ticket to ride!")
