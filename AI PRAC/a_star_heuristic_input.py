# A* with User Input (Start, Goal + Heuristic)
import heapq
def a_star(graph, heuristic, start, goal):
    queue = [(0, start)]
    cost = {start: 0}
    parent = {start: None}
    visited = set()
    nodes = 0
    while queue:
        f, current = heapq.heappop(queue)
        nodes += 1
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("\nGoal Reached!")
            print("Path:", path)
            print("Total Cost:", cost[goal])
            print("Nodes Explored:", nodes)
            return
        visited.add(current)
        for neighbor, edge_cost in graph[current]:
            if neighbor in visited:
                continue
            new_cost = cost[current] + edge_cost
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                heapq.heappush(
                    queue,
                    (new_cost + heuristic[neighbor], neighbor)
                )
    print("No Path Found")
# Fixed Graph
graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 4), ('D', 1)],
    'B': [('E', 3), ('F', 1)],
    'E': [('H', 5)],
    'F': [('I', 2), ('G', 3)],
    'C': [], 'D': [], 'H': [], 'I': [], 'G': []
}
# User Input
start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")
print("\nEnter Heuristic Values:")
heuristic = {}
for node in graph:
    heuristic[node] = int(
        input(f"Heuristic value for {node}: ")
    )
# Run A*
a_star(graph, heuristic, start, goal)
