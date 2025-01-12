code = input("Enter the room code:").title()

rooms = {
    "Main Reception": "at the main entrance of the A block",
    "Staffroom": "on the top floor of the B block",
    "Sports Hall": "on the side of the B Block",
    "Dance Studio": "on the ground floor in the A Block",
    "Activity Studio": "on the ground floor in the A Block"
}

# Check if the code is valid (either a room code or a room name)
while len(code) > 4 or not code[0].isalpha():
    if code not in rooms:  # Invalid input not in rooms dictionary
        print("Room number is invalid. Please enter a valid room number.")
        code = input("Enter the room code:").title()
    else:
        break  # Room name found in the dictionary, exit loop

# If the code is a room number (i.e., it has a number after the first character)
if code[0].isalpha() and code[1:].isdigit():
    Floor = int(code[1:])  # Extract floor number from the code (e.g., "A203" -> 203)

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

# If the code is a room name from the dictionary
elif code in rooms:
    print("This room is located " + rooms[code])

else:
    print("We cannot locate this room! Are you sure this is a valid room?")