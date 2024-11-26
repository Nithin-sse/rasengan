def is_valid(node, color, graph, coloring):
    return all(coloring.get(neighbor) != color for neighbor in graph[node])

def color_map(graph, colors, coloring={}, nodes=None):
    if len(coloring) == len(graph):
        return coloring
    nodes = nodes or list(graph.keys())
    node = nodes[0]
    for color in colors:
        if is_valid(node, color, graph, coloring):
            coloring[node] = color
            result = color_map(graph, colors, coloring, nodes[1:])
            if result:
                return result
            del coloring[node]
    return None

# Input graph
n = int(input("Enter the number of regions: "))
graph = {input("Enter region: "): input(f"Enter neighbors of this region (space-separated): ").split() for _ in range(n)}
colors = input("Enter available colors (space-separated): ").split()

# Solve CSP
solution = color_map(graph, colors)
print("Solution:", solution if solution else "No solution found")
