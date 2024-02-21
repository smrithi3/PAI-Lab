import itertools

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def brute_force_tsp(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))

    # Generate all possible permutations of cities
    all_permutations = itertools.permutations(cities)

    # Initialize variables to track the best solution
    best_path = None
    best_distance = float('inf')

    # Iterate through all permutations and calculate total distances
    for permutation in all_permutations:
        current_distance = calculate_total_distance(permutation, distances)

        # Update the best solution if a shorter path is found
        if current_distance < best_distance:
            best_distance = current_distance
            best_path = permutation

    return best_path, best_distance

# Example usage:
# Replace 'distances' with your own distance matrix
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

best_path, best_distance = brute_force_tsp(distances)

print("Best TSP Path:", best_path)
print("Total Distance:", best_distance)
