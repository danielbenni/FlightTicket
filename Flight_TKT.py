available_seats = {
    "Economy": {"A1": True, "A2": False, "B1": True, "B2": True},
    "Business": {"C1": False, "C2": True, "D1": True, "D2": False}
}

def display_status():
    print("Available Seats:")
    print("{:<10} {:<10} {:<10}".format("Class", "Seat No.", "Status"))
    for class_name, seats in available_seats.items():
        for seat_no, status in seats.items():
            print("{:<10} {:<10} {:<10}".format(class_name, seat_no, "Available" if status else "Booked"))

def change_status(class_name, seat_no):
    if available_seats[class_name][seat_no]:
        available_seats[class_name][seat_no] = False
        print(f"Seat {seat_no} in {class_name} class successfully booked.")
    else:
        print(f"Seat {seat_no} in {class_name} class is already booked.")
