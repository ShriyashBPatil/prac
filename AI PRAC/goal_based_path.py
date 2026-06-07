# Goal-Based Agent for Path Planning
graph = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "Goal"
}
def goal_based_agent(start, goal):
    path = [start]
    while start != goal:
        start = graph[start]
        path.append(start)
    return path
# Run Agent
result = goal_based_agent("A", "Goal")
print("Path followed by agent:")
print(" -> ".join(result))
