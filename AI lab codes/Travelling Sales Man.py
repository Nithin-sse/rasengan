from itertools import permutations

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_cost, best_path = float('inf'), []
    for perm in permutations(nodes):
        path = [start] + list(perm) + [start]
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        if cost < min_cost:
            min_cost, best_path = cost, path
    return min_cost, best_path

# User input
n = int(input("Enter the number of nodes: "))
graph = {}
nodes = input("Enter the node labels (space-separated): ").split()
for node in nodes:
    graph[node] = {neighbor: int(cost) for neighbor, cost in zip(nodes, input(f"Enter costs from {node} to {', '.join(nodes)} (space-separated): ").split())}

start = input("Enter the starting node: ")
cost, path = tsp(graph, start)
print(f"Minimum cost: {cost}\nPath: {' -> '.join(path)}")
