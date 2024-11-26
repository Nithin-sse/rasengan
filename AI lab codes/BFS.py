from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start], 0)])
    visited = {start}
    
    while queue:
        node, path, cost = queue.popleft()
        if node == end:
            return path, cost
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], cost + weight))
    
    return None, float('inf')

# Input graph
graph = {input("Node: "): [(n.split(",")[0], int(n.split(",")[1])) 
           for n in input("Neighbors (node,weight): ").split()]
         for _ in range(int(input("Number of nodes: ")))}

start, end = input("Start: "), input("End: ")
path, cost = bfs_shortest_path(graph, start, end)

print(f"Path: {' -> '.join(path)} with cost {cost}" if path else f"No path from {start} to {end}.")
