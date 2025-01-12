while True:  # Infinite loop to keep asking for requests
    code = input("Enter the room code (or type 'exit' to quit): ").title()

    if code == 'Exit':
        print("Exiting the program...")
        break  # Exit the loop if the user types 'exit'

    # Process the code as needed
    rooms = {
        "Main Reception": "at the main entrance of the A block",
        "Staffroom": "on the top floor of the B block",
        "Sports Hall": "on the side of the B Block",
        "Dance Studio": "on the ground floor in the A Block",
        "Activity Studio": "on the ground floor in the A Block"
    }

    while len(code) > 4 or not code[0].isalpha():
        if code not in rooms:
            print("Room number is invalid. Please enter a valid room number.")
            code = input("Enter the room code:").title()
        else:
            break

    # Process the floor number or the room name as described earlier
    if code[0].isalpha() and code[1:].isdigit():
        Floor = int(code[1:])
        if code[0] == "S":
            print("Room is in the 6th form block.")
        else:
            print("Room is in the", code[0], "block.")
        
        if Floor >= 0 and Floor < 100:
            print("Room is on the ground floor.")
        elif Floor >= 100 and Floor < 200:
            print("Room is on the first floor.")
        elif Floor >= 200:
            print("Room is on the second floor.")

    elif code in rooms:
        print("This room is located " + rooms[code])
    else:
        print("We cannot locate this room! Are you sure this is a valid room?")