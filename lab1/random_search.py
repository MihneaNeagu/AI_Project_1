import numpy as np
import time


def generate_random_solution(num_objects):
    return np.random.randint(2, size=num_objects)


def is_valid(solution, weights, max_weight):
    total_weight = np.sum(solution * weights)
    return total_weight <= max_weight


def evaluate_solution(solution, values):
    return np.sum(solution * values)


def random_search(num_objects, values, weights, max_weight, iterations):
    for _ in range(10):  # 10 rulari
        best_solution = None
        best_score = float('-inf')
        valid_scores = []
        start_time = time.time()
        for _ in range(iterations):
            solution = generate_random_solution(num_objects)
            if is_valid(solution, weights, max_weight):
                score = evaluate_solution(solution, values)
                valid_scores.append(score)  # Collect scores of valid solutions
                if score > best_score:
                    best_solution = solution
                    best_score = score

    end_time = time.time()
    runtime = end_time - start_time

    # Calculate average score of valid solutions
    average_valid_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0

    return best_solution, best_score, runtime, average_valid_score


def parse_rucksack_data(file_path):
    values = []
    weights = []
    max_weight = None
    num_objects = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Extracting num_objects from the first line
        num_objects = int(lines[0])

        # Iterating through the rest of the lines
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 3:
                values.append(int(parts[1]))
                weights.append(int(parts[2]))
            elif len(parts) == 1:
                max_weight = int(parts[0])

    return num_objects, values, weights, max_weight


def main_random_search():
    num_objects = 5
    values = np.array([10, 5, 15, 7, 6])
    weights = np.array([2, 3, 5, 7, 1])
    max_weight = 10
    iterations = 10000

    best_solution, best_score, runtime, average_valid_score = random_search(num_objects, values, weights, max_weight,
                                                                            iterations)

    print("Random Search Algorithm Results:")
    print("Best Solution:", best_solution)
    print("Best Score:", best_score)
    print("Average score:", average_valid_score)
    print("Runtime:", runtime, "seconds")


if __name__ == "__main__":
    main_random_search()
