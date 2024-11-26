from collections import deque

def water_jug_solver(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0)])  # Starting with both jugs empty
    path = []

    while queue:
        state = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path.append(state)

        jug1, jug2 = state
        if jug1 == target or jug2 == target:
            path.append(state)
            return path

        # Possible moves
        next_states = [
            (capacity1, jug2),  # Fill jug1
            (jug1, capacity2),  # Fill jug2
            (0, jug2),          # Empty jug1
            (jug1, 0),          # Empty jug2
            (min(jug1 + jug2, capacity1), max(0, jug1 + jug2 - capacity1)),  # Pour jug2 -> jug1
            (max(0, jug1 + jug2 - capacity2), min(jug1 + jug2, capacity2))   # Pour jug1 -> jug2
        ]

        for next_state in next_states:
            if next_state not in visited:
                queue.append(next_state)

    return None  # No solution found

# Input from user
capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter the target amount: "))

# Solve the problem
solution = water_jug_solver(capacity1, capacity2, target)

# Output the result
if solution:
    print("\nSolution Path:")
    for step in solution:
        print(f"Jug 1: {step[0]}, Jug 2: {step[1]}")
else:
    print("No solution found.")
