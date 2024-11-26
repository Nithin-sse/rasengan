def min_max(node, depth, is_maximizing):
    if isinstance(node, int):  # Leaf node
        return node
    if is_maximizing:
        return max(min_max(child, depth + 1, False) for child in node)
    else:
        return min(min_max(child, depth + 1, True) for child in node)

# Input: User defines a game tree
try:
    tree = eval(input("Enter a game tree (e.g., [[3, 5], [2, 9]]): "))
    is_maximizing = input("Start as maximizing? (yes/no): ").strip().lower() == "yes"
    print("Optimal value:", min_max(tree, 0, is_maximizing))
except Exception as e:
    print(f"Invalid input: {e}")
 
