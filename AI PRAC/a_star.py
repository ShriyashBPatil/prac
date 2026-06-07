# A* Search Algorithm
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
            print("Goal Reached!")
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
# Graph
graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 4), ('D', 1)],
    'B': [('E', 3), ('F', 1)],
    'E': [('H', 5)],
    'F': [('I', 2), ('G', 3)],
    'C': [], 'D': [], 'H': [], 'I': [], 'G': []
}
# Heuristic Values
heuristic = {
    'S': 13, 'A': 12, 'B': 4,
    'C': 7, 'D': 3, 'E': 8,
    'F': 2, 'H': 4, 'I': 9, 'G': 0
}
start = 'S'
goal = 'G'
print("Start Node:", start)
print("Goal Node:", goal)
a_star(graph, heuristic, start, goal)
