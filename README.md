# goit-algo2-hw-09
The repository for the 9th GoItNeo Design and Analysis of Algorithms homework

### Task: Implement a program to minimize the Sphere function \( f(x) = \sum_{i=1}^{n} x_i^2 \), using three different approaches to local optimization:

- The "Hill Climbing" Algorithm

- Random Local Search

- Simulated Annealing

#### Requirements:
1. The limits of the function are defined as xi∈[−5,5] for each parameter xi.

2. The algorithms should return the optimal point (list of x coordinates) and the function value at this point.

3. Implement three optimization methods:
- hill_climbing — hill climbing algorithm.

- random_local_search — random local search.

- simulated_annealing — simulated annealing.

4. Each algorithm must accept the parameter iterations, which determines the maximum number of iterations for the algorithm to execute.

5. The algorithms must complete execution under one of the conditions:

- The change in the value of the objective function or the position of the point in the solution space between two consecutive iterations becomes less than epsilon, where epsilon is a precision parameter and determines the algorithm's sensitivity to minor improvements.

- For the simulated annealing algorithm, temperature is taken into account: if the temperature decreases to a value less than epsilon, the algorithm terminates, as this indicates the exhaustion of the algorithm's search capability.

#### Results:

**Hill Climbing:**

Solution: (0.00013644312680850118, 0.000718703244076753), Value: 5.351510798997294e-07

Observation: Hill Climbing found a solution close to the global minimum, with a very small function value. This indicates that the algorithm was able to make significant progress towards minimizing the sphere function, although it may not have reached the global minimum due to local minima and stopping criteria.
**Random Local Search:**

Solution: (0.0010216506720544527, -0.0077837303066841945), Value: 6.163022758290335e-05

Observation: Random Local Search was able to find a solution that is further from the global minimum compared to Hill Climbing, with a larger function value. The algorithm uses random exploration, so it can often settle in suboptimal solutions depending on the starting point and exploration behavior.

**Simulated Annealing:**

Solution: (-0.010517139631220841, 0.001681560120088084), Value: 0.0001134378704600667

Observation: Simulated Annealing provided a solution that is somewhat better than the Random Local Search, but still not as close to the global minimum as Hill Climbing. The temperature decay and probabilistic acceptance of worse solutions allowed it to explore different areas of the search space more effectively, though it didn't converge to the global minimum.

#### Summary:

- Hill Climbing performed the best in terms of finding the smallest function value, suggesting it efficiently navigated towards the minimum. However, its performance may depend on the starting point, and it could get stuck in local minima.

- Random Local Search showed more exploration but did not find as optimal a solution as Hill Climbing. Its performance is highly dependent on random exploration and can vary significantly.

- Simulated Annealing provided a balance between exploration and exploitation, but still didn’t outperform Hill Climbing in this particular test case.

In conclusion, while all three methods contributed to minimizing the sphere function, Hill Climbing proved to be the most effective in this context, potentially due to its greedy approach of moving towards the best neighbor. However, depending on the problem landscape, a combination of methods or different parameter tuning might yield better results.