from itertools import permutations

def crypt_arithmetic_solver():
    # Get the cryptarithmic problem from the user
    problem = input("Enter the cryptarithmic equation (e.g., SEND + MORE == MONEY): ")
    letters = sorted(set(filter(str.isalpha, problem)))  # Extract unique letters
    
    # Ensure there are at most 10 unique letters
    if len(letters) > 10:
        print("Error: Too many unique letters (maximum is 10).")
        return
    
    # Try all permutations of digits for the unique letters
    for perm in permutations(range(10), len(letters)):
        # Create a mapping of letters to digits
        substitution = str.maketrans("".join(letters), "".join(map(str, perm)))
        translated = problem.translate(substitution)
        
        # Check for leading zeros in any number
        if any(word[0] == '0' for word in translated.replace(" ", "").split("==")[0].split("+") if word.isalnum()):
            continue
        
        # Evaluate the translated problem
        try:
            if eval(translated):
                print(f"Solution: {translated}")
                return
        except:
            continue
    
    print("No solution found.")

# Run the solver
crypt_arithmetic_solver()

