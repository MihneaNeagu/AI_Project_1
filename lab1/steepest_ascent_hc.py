import numpy as np
import time


def generate_random_solution(num_objects):
    return np.random.randint(2, size=num_objects)


def is_valid(solution, weights, max_weight):
    total_weight = np.sum(solution * weights)
    return total_weight <= max_weight


def evaluate_solution(solution, values):
    return np.sum(solution * values)


def get_neighborhood(current_solution):
    neighborhood = []
    num_objects = len(current_solution)

    for i in range(num_objects):
        neighbor = np.copy(current_solution)
        neighbor[i] = 1 - neighbor[i]  # Bit swap
        neighborhood.append(neighbor)

    return neighborhood


def sahc(num_objects, values, weights, max_weight, iterations):
    for _ in range(10): # 10 rulari
        best_score = float('-inf')
        valid_scores = []
        valid_weights = []
        start_time = time.time()
        for k in range(iterations):
            current_solution = generate_random_solution(num_objects)
            current_score = evaluate_solution(current_solution, values)

            for _ in range(iterations):
                neighborhood = get_neighborhood(current_solution)
                found_better = False
                for neighbor in neighborhood:
                    if is_valid(neighbor, weights, max_weight):
                        neighbor_score = evaluate_solution(neighbor, values)
                        if neighbor_score > current_score:
                            current_solution = neighbor
                            current_score = neighbor_score
                            found_better = True
                            break  # Move to the next iteration if a better neighbor is found
                if not found_better:
                    break  # Break out if no better neighbor is found

            # Update best solution and score if necessary
            if current_score > best_score:
                best_solution = current_solution
                best_score = current_score
            # Collect scores and weights of valid solutions
            if is_valid(current_solution, weights, max_weight):
                valid_scores.append(current_score)
                valid_weights.append(np.sum(current_solution * weights))
    end_time = time.time()
    runtime = end_time - start_time
    # Calculate average score and weight of valid solutions
    average_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0
    average_weight = sum(valid_weights) / len(valid_weights) if valid_weights else 0
    return iterations, average_score, average_weight, best_score, runtime, best_solution


def parse_rucksack_data(file_path):
    values = []
    weights = []
    max_weight = None
    num_objects = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

        num_objects = int(lines[0])

        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 3:
                values.append(int(parts[1]))
                weights.append(int(parts[2]))
            elif len(parts) == 1:
                max_weight = int(parts[0])

    return num_objects, values, weights, max_weight

def main_sahc():
    file_path = "data.txt"
    num_objects, values, weights, max_weight = parse_rucksack_data(file_path)
    iterations = 1000

    k, avg_score, avg_weight, best_score, runtime, best_solution = sahc(num_objects, np.array(values), np.array(weights), max_weight, iterations)

    print("SAHC Algorithm Results:")
    print("k (iterations):", k)
    print("Average Score:", avg_score)
    print("Average Weight:", avg_weight)
    print("Best Score:", best_score)
    print("Runtime:", runtime, "seconds")
    print("Best Solution:", best_solution)

if __name__ == "__main__":
    main_sahc()
