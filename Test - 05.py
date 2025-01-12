while True:  # Infinite loop to keep asking for requests
    code = input("Enter the room code (or type 'exit' to quit): ").title()

    if code.lower() == 'exit':
        print("Exiting the program...")
        break  # Exit the loop if the user types 'exit'

    rooms = {
        "Main Reception": "at the main entrance of the A block",
        "Staffroom": "on the top floor of the B block",
        "Sports Hall": "on the side of the B Block",
        "Dance Studio": "on the ground floor in the A Block",
        "Activity Studio": "on the ground floor in the A Block"
    }

    # Validate the room code input
    while len(code) > 4 or not code[0].isalpha():
        if code not in rooms:
            print("Room number is invalid. Please enter a valid room number.")
            code = input("Enter the room code:").title()
        else:
            break

    # If the code is a room number (e.g., A203, B150)
    if code[0].isalpha() and code[1:].isdigit():
        floor = int(code[1:])  # Extract the floor number

        # Check if the floor number is valid based on the building type
        if code[0] == "S":
            if floor > 199:
                print("Invalid floor number for the S building. Floor must be between 0 and 199.")
                continue  # Ask for the input again
            else:
                print("Room is in the 6th form block.")

        elif code[0] in ["A", "B", "C"]:
            if floor > 299:
                print("Invalid floor number for the A, B, or C buildings. Floor must be between 0 and 299.")
                continue  # Ask for the input again
            else:
                print(f"Room is in the {code[0]} block.")

        # Display floor information
        if floor >= 0 and floor < 100:
            print("Room is on the ground floor.")
        elif floor >= 100 and floor < 200:
            print("Room is on the first floor.")
        elif floor >= 200:
            print("Room is on the second floor.")

    # If the code is a room name from the dictionary
    elif code in rooms:
        print("This room is located " + rooms[code])
    else:
        print("We cannot locate this room! Are you sure this is a valid room?")