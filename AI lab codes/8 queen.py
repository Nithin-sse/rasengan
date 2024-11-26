def solve_n_queens(n, board=[], results=[]):
    if len(board) == n:
        results.append(board)
        return
    for col in range(n):
        if all(col != c and abs(len(board) - r) != abs(col - c) for r, c in enumerate(board)):
            solve_n_queens(n, board + [col], results)

def print_board(solution):
    for row in solution:
        print("".join("Q" if i == row else "." for i in range(len(solution))))
    print()

if __name__ == "__main__":
    n = int(input("Enter the number of queens (default 8): ") or 8)
    results = []
    solve_n_queens(n, results=results)
    print(f"Found {len(results)} solutions:")
    for sol in results:
        print_board(sol)
