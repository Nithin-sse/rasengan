def alpha_beta(node, depth, alpha, beta, is_maximizing):
    if isinstance(node, int):  # Leaf node
        return node
    if is_maximizing:
        value = float('-inf')
        for child in node:
            value = max(value, alpha_beta(child, depth + 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node:
            value = min(value, alpha_beta(chi  ld, depth + 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

# Input: User defines a game tree
try:
    tree = eval(input("Enter a game tree (e.g., [[3, 5], [2, 9]]): "))
    is_maximizing = input("Start as maximizing? (yes/no): ").strip().lower() == "yes"
    print("Optimal value:", alpha_beta(tree, 0, float('-inf'), float('inf'), is_maximizing))
except Exception as e:
    print(f"Invalid input: {e}")
