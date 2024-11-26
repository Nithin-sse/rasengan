from collections import deque

def is_valid_state(m_left, c_left, m_right, c_right):
    # Ensure all counts are non-negative and no side violates the missionaries < cannibals condition
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0 or
        (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right)):
        return False
    return True

def bfs():
    # Initial state: (missionaries_left, cannibals_left, boat_position)
    initial_state = (3, 3, 1)  # Start with all on the left and boat on the left
    goal_state = (0, 0, 0)     # Goal is to have everyone on the right
    queue = deque([(initial_state, [])])  # BFS queue
    visited = set()            # Track visited states to avoid loops

    while queue:
        (m_left, c_left, boat_position), path = queue.popleft()

        # Check if we've reached the goal state
        if (m_left, c_left, boat_position) == goal_state:
            return path

        # Skip already visited states
        if (m_left, c_left, boat_position) in visited:
            continue
        visited.add((m_left, c_left, boat_position))

        # Define possible moves of the boat
        possible_moves = [
            (1, 0), (2, 0),  # One or two missionaries
            (0, 1), (0, 2),  # One or two cannibals
            (1, 1)           # One missionary and one cannibal
        ]

        for m_move, c_move in possible_moves:
            if boat_position == 1:  # Boat on the left side
                new_m_left, new_c_left = m_left - m_move, c_left - c_move
                new_m_right, new_c_right = 3 - new_m_left, 3 - new_c_left
                if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                    new_state = (new_m_left, new_c_left, 0)
                    new_path = path + [f"Left: {new_m_left}m {new_c_left}c | Right: {new_m_right}m {new_c_right}c | Boat: 0 (right)"]
                    queue.append((new_state, new_path))
            else:  # Boat on the right side
                new_m_left, new_c_left = m_left + m_move, c_left + c_move
                new_m_right, new_c_right = 3 - new_m_left, 3 - new_c_left
                if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                    new_state = (new_m_left, new_c_left, 1)
                    new_path = path + [f"Left: {new_m_left}m {new_c_left}c | Right: {new_m_right}m {new_c_right}c | Boat: 1 (left)"]
                    queue.append((new_state, new_path))

    return None  # No solution found

# Run the BFS to find the solution
solution = bfs()
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
