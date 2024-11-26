def vacuum_cleaner():
    # Get room conditions at runtime
    rooms = {
        "A": input("Enter status of room A (clean/dirty): ").strip().lower(),
        "B": input("Enter status of room B (clean/dirty): ").strip().lower()
    }
    current_room = input("Enter starting room (A/B): ").strip().upper()
    
    # Action sequence
    actions = []
    while "dirty" in rooms.values():
        if rooms[current_room] == "dirty":
            actions.append(f"Clean {current_room}")
            rooms[current_room] = "clean"
        else:
            current_room = "A" if current_room == "B" else "B"
            actions.append(f"Move to {current_room}")
    
    print("Actions:", " -> ".join(actions))
    print("All rooms are clean!")

# Run the vacuum cleaner simulation
vacuum_cleaner()
