from heapq import heappop, heappush

def a_star_search(graph, heuristic, start, goal):
    open_list = [(0 + heuristic[start], start, [start])]  # (f, node, path)
    visited = set()

    while open_list:
        f, current, path = heappop(open_list)

        if current == goal:
            return path, f - heuristic[current]

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g = f - heuristic[current] + cost
                heappush(open_list, (g + heuristic[neighbor], neighbor, path + [neighbor]))

    return None, None

# Input graph and heuristic values
n = int(input("Enter the number of nodes: "))
graph = {}
heuristic = {}

print("Enter edges in the format 'node1 node2 cost' (one per line, type 'done' to stop):")
while True:
    edge = input().strip()
    if edge == "done":
        break
    u, v, cost = edge.split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

print("Enter heuristic values for each node (format 'node h_value'):")
for _ in range(n):
    node, h = input().split()
    heuristic[node] = int(h)

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

# Perform A* search
path, cost = a_star_search(graph, heuristic, start, goal)

# Output the result
if path:
    print(f"\nPath found: {' -> '.join(path)} with cost: {cost}")
else:
    print("No path found.")
