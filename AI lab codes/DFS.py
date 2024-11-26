def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# User input
graph = {input("Enter node: "): input("Enter neighbors (space-separated): ").split() for _ in range(int(input("Enter number of nodes: ")))}
start = input("Enter starting node: ")
print("DFS traversal:")
dfs(graph, start)
