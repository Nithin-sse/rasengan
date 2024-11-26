import heapq
import itertools

# Helper functions
def is_solvable(state):
    """Check if the puzzle is solvable."""
    inversions = 0
    flat_state = [tile for tile in state if tile != 0]
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    return inversions % 2 == 0

def manhattan_distance(state, goal):
    """Calculate the Manhattan distance heuristic."""
    distance = 0
    for i in range(1, 9):  # Numbers 1 through 8
        current_idx = state.index(i)
        goal_idx = goal.index(i)
        distance += abs(current_idx // 3 - goal_idx // 3) + abs(current_idx % 3 - goal_idx % 3)
    return distance

def generate_successors(state):
    """Generate all possible successor states."""
    def swap(state, i, j):
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return tuple(state)

    neighbors = []
    zero_index = state.index(0)
    x, y = zero_index // 3, zero_index % 3  # Convert 1D index to 2D
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx * 3 + ny
            neighbors.append(swap(state, zero_index, new_index))
    return neighbors

def a_star(start, goal):
    """A* algorithm to solve the 8-puzzle problem."""
    if not is_solvable(start):
        return "The puzzle is not solvable."
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, goal)}
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in generate_successors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                if neighbor not in [item[1] for item in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return "No solution found."

# Main program
if __name__ == "__main__":
    # Input the start and goal states
    print("Enter the start state as a space-separated list (0 for the blank tile):")
    start = tuple(map(int, input().split()))
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Default goal state

    # Ensure valid input
    if len(start) != 9 or set(start) != set(range(9)):
        print("Invalid input. Please provide exactly 9 unique numbers (0-8).")
    else:
        solution = a_star(start, goal)
        if isinstance(solution, str):
            print(solution)
        else:
            print("Solution found:")
            for step in solution:
                print(step[:3])
                print(step[3:6])
                print(step[6:])
                print()
