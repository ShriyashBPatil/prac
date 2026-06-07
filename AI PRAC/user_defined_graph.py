# User-Defined Graph
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    graph[node] = input("Enter neighbors (space separated): ").split()
print("Graph entered:")
print(graph)
