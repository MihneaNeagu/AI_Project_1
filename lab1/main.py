import numpy as np
from random_search import random_search
from steepest_ascent_hc import sahc, parse_rucksack_data

def main_random_search():
    num_objects = 5
    values = np.array([10, 5, 15, 7, 6])
    weights = np.array([2, 3, 5, 7, 1])
    max_weight = 10
    iterations = 10000

    best_solution, best_score, runtime, average_valid_score = random_search(num_objects, values, weights, max_weight, iterations)

    print("Random Search Algorithm Results:")
    print("Best Solution:", best_solution)
    print("Best Score:", best_score)
    print("Average score:", average_valid_score)
    print("Runtime:", runtime, "seconds")

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
    while True:
        print("\nMenu:")
        print("1. Random Search Algorithm")
        print("2. SAHC Algorithm")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            main_random_search()
        elif choice == "2":
            main_sahc()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
