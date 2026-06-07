# Goal-Based Agent with Input Validation
graph = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "Goal",
    "Goal": None
}
def goal_based_agent(start, goal):
    path = [start]
    while start != goal:
        start = graph[start]
        path.append(start)
    return path
# User Input
start = input("Enter Start State: ")
goal = input("Enter Goal State: ")
# Validation
if start not in graph or goal not in graph:
    print("Error: Start or Goal state not present in graph.")
else:
    result = goal_based_agent(start, goal)
    print("Path followed by agent:")
    print(" -> ".join(result))
