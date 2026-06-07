# Goal-Based Agent with Step Counter
graph = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "Goal"
}
def goal_based_agent(start, goal):
    path = [start]
    steps = 0
    while start != goal:
        start = graph[start]
        path.append(start)
        steps += 1
    return path, steps
# Run Agent
result, steps = goal_based_agent("A", "Goal")
print("Path followed by agent:")
print(" -> ".join(result))
print("Total number of moves:", steps)
