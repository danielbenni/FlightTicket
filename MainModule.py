from Flight_TKT import display_status, change_status

# Display the following options for the user to select
while True:
    print("Options:")
    print("a. Display Status")
    print("b. Change Status")
    print("Enter your Choice (a/b): ", end="")
    
    # Get user input for choice
    choice = input().lower()

    # Call the respective functions based on user choice
    if choice == 'a':
        display_status()
    elif choice == 'b':
        class_input = input("Enter Class (Economy/Business): ").capitalize()
        seat_input = input("Enter Seat Number: ")
        change_status(class_input, seat_input)
    else:
        print("Invalid choice. Please enter 'a' or 'b'.")
    
    # Ask if the user wants to continue
    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice.lower() != 'y':
        break
