from handler import hill_climbing, random_local_search, simulated_annealing, sphere_function

def main():
    # Define bounds for the function
    bounds = [(-5, 5), (-5, 5)]

    # Run Hill Climbing algorithm
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print(f"Solution: {hc_solution}, Value: {hc_value}")

    # Run Random Local Search algorithm
    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print(f"Solution: {rls_solution}, Value: {rls_value}")

    # Run Simulated Annealing algorithm
    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print(f"Solution: {sa_solution}, Value: {sa_value}")

if __name__ == "__main__":
    main()
