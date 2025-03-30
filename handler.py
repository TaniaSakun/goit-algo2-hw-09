import random
import math
from typing import List, Tuple

# Define the sphere function f(x) = sum(x_i^2)
def sphere_function(x: List[float]) -> float:
    return sum(xi ** 2 for xi in x)

# Get a random starting point within the bounds
def random_solution(bounds: List[Tuple[float, float]]) -> List[float]:
    return [random.uniform(lb, ub) for lb, ub in bounds]

# Hill Climbing Algorithm
def hill_climbing(func, bounds, iterations=10000, epsilon=1e-6):
    # Ensure the current point is a list
    current_point = random_solution(bounds)
    current_point = list(current_point)  # Convert it to a list
    current_value = func(current_point)

    # define neighbour points
    def get_neighbors(current, bounds, step=0.001):
        neighbors = []
        for i, (lb, ub) in enumerate(bounds):
            new_point = list(current)  # Create a copy of current as a list
            new_point[i] = max(min(current[i] + step, ub), lb)  # Modify the value in the list
            neighbors.append(tuple(new_point))  # Convert back to tuple when appending

            new_point[i] = max(min(current[i] - step, ub), lb)
            neighbors.append(tuple(new_point))  # Convert back to tuple when appending
        return neighbors

    for _ in range(iterations):
        neighbors = get_neighbors(current_point, bounds)

        # find the best neighbour
        next_point = None
        next_value = float('inf')

        for neighbor in neighbors:
            value = func(neighbor)
            if value < next_value:
                next_point = neighbor
                next_value = value

        # stopping criteria
        if abs(current_value - next_value) < epsilon or math.dist(current_point, next_point) < epsilon or next_point is None:
            break

        # switch to better neighbour
        current_point, current_value = next_point, next_value

    return current_point, current_value

# Random Local Search Algorithm
def random_local_search(func, bounds: List[Tuple[float, float]], probability: float = 0.2, iterations: int = 10000, epsilon: float = 1e-6) -> Tuple[List[float], float]:
    current_point = random_solution(bounds)
    current_value = func(current_point)

    # Get random neighbor within the bounds
    def get_random_neighbor(current: List[float], bounds: List[Tuple[float, float]], step_size: float = 0.1) -> Tuple[float, float]:
        return tuple(max(min(current[i] + random.uniform(-step_size, step_size), ub), lb) for i, (lb, ub) in enumerate(bounds))

    for _ in range(iterations):
        new_point = get_random_neighbor(current_point, bounds)
        new_value = func(new_point)

        # Stopping criteria
        if abs(current_value - new_value) < epsilon or math.dist(current_point, new_point) < epsilon:
            break

        # Switch to the new point, always move if the new value is better
        if new_value < current_value or random.random() < probability:
            current_point, current_value = new_point, new_value

    return current_point, current_value

# Simulated Annealing Algorithm
def simulated_annealing(func, bounds: List[Tuple[float, float]], iterations: int = 10000, temp: float = 1000, cooling_rate: float = 0.98, epsilon: float = 1e-6) -> Tuple[List[float], float]:
    current_solution = random_solution(bounds)
    current_energy = func(current_solution)

    # Get random neighbor within the bounds
    def get_neighbor(current: List[float], bounds: List[Tuple[float, float]], step_size: float = 0.1) -> Tuple[float, float]:
        return tuple(max(min(current[i] + random.uniform(-step_size, step_size), ub), lb) for i, (lb, ub) in enumerate(bounds))

    # Main optimization loop
    for _ in range(iterations):
        if temp < epsilon:  # If temperature is too low, stop early
            break

        new_solution = get_neighbor(current_solution, bounds)
        new_energy = func(new_solution)
        delta_energy = new_energy - current_energy

        # Accept new solution if it's better, or with a probability depending on temperature
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temp):
            current_solution = new_solution
            current_energy = new_energy

        temp *= cooling_rate  # Cooling step

    return current_solution, current_energy
