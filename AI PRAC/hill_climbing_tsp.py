# Hill Climbing Algorithm for Travelling Salesman Problem(TSP)
import random
# Distance Matrix
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
def total_distance(tour):
    cost = 0
    for i in range(len(tour)):
        cost += dist_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return cost
def get_neighbor(tour):
    new_tour = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour
def hill_climbing(max_iter=1000):
    current = list(range(len(dist_matrix)))
    random.shuffle(current)
    current_cost = total_distance(current)
    for _ in range(max_iter):
        neighbor = get_neighbor(current)
        neighbor_cost = total_distance(neighbor)
        if neighbor_cost < current_cost:
            current = neighbor
            current_cost = neighbor_cost
    return current, current_cost

# Run Algorithm
solution, cost = hill_climbing()
print("Best Tour:", solution)
print("Cost:", cost)
