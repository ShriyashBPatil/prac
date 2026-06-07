import os

files = {
"vacuum_agent_simple.py": r'''# Simple Reactive Agent (Vacuum Cleaner World)
class SimpleAgent:
    def decide(self, environment):
        if environment == "dirty":
            return "clean"
        else:
            return "move"
environment = "dirty"
agent = SimpleAgent()
action = agent.decide(environment)
print("Agent action:", action)
''',

"vacuum_agent_input.py": r'''# Vacuum Cleaner Agent Using User Input
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Suck"
    location = location.upper()
    if location == "A":
        return "Move Right to B"
    elif location == "B":
        return "Move Right to C"
    elif location == "C":
        return "Move Left to B"
    else:
        return "Invalid Location"
# User Input
location = input("Enter Location (A/B/C): ")
status = input("Enter Status (clean/dirty): ")
# Agent Action
print("Action:", vacuum_agent(location, status))
''',

"vacuum_agent_two_rooms.py": r'''# Vacuum Cleaner Agent for Two Rooms
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Suck"
    if location == "A":
        return "Move Right"
    else:
        return "Move Left"
# Test Cases
for location in ["A", "B"]:
    for status in ["clean", "dirty"]:
        print(
            f"Location: {location}, Status: {status}, Action: {vacuum_agent(location, status)}"
        )
''',

"vacuum_agent_three_rooms.py": r'''# Vacuum Cleaner Agent for Three Rooms
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Suck"
    location = location.upper()
    if location == "A":
        return "Move Right"
    elif location == "B":
        return "Move Right"
    elif location == "C":
        return "Move Left"
    else:
        return "Invalid Location"
# Test Cases
for location in ["A", "B", "C"]:
    for status in ["clean", "dirty"]:
        print(
            f"Location: {location}, Status: {status}, Action: {vacuum_agent(location, status)}"
        )
''',

"goal_based_path.py": r'''# Goal-Based Agent for Path Planning
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
''',

"goal_based_validation.py": r'''# Goal-Based Agent with Input Validation
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
''',

"goal_based_step_counter.py": r'''# Goal-Based Agent with Step Counter
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
''',

"user_defined_graph.py": r'''# User-Defined Graph
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    graph[node] = input("Enter neighbors (space separated): ").split()
print("Graph entered:")
print(graph)
''',

"goal_based_user_input.py": r'''# Goal-Based Agent with User Input
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
# User Input
start = input("Enter Start State: ")
goal = input("Enter Goal State: ")
# Run Agent
result = goal_based_agent(start, goal)
print("Path followed by agent:")
print(" -> ".join(result))
''',

"8_puzzle_dfs.py": r'''# 8-Puzzle Problem using DFS
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class PuzzleState:
    def __init__(self, board, x, y, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.parent = parent
    def is_goal(self):
        return self.board == goal
def print_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    path.reverse()
    print("\nSolution Path:\n")
    for i, board in enumerate(path):
        print("Step", i)
        for row in board:
            print(*row)
        print()
    print("Total Moves:", len(path) - 1)
def dfs(start, x, y):
    stack = [PuzzleState(start, x, y)]
    visited = {tuple(map(tuple, start))}
    while stack:
        current = stack.pop()
        if current.is_goal():
            print("Goal State Found")
            print_path(current)
            return
        for dx, dy in moves:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in current.board]
                new_board[current.x][current.y], new_board[nx][ny] = \
                    new_board[nx][ny], new_board[current.x][current.y]
                state = tuple(map(tuple, new_board))
                if state not in visited:
                    visited.add(state)
                    stack.append(
                        PuzzleState(new_board, nx, ny, current)
                    )
    print("No Solution Found")
# Initial State
start = [
    [4, 2, 3],
    [1, 0, 5],
    [6, 8, 7]
]
dfs(start, 1, 1)
''',

"8_puzzle_dfs_input.py": r'''# 8-Puzzle Using DFS with User Input
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class PuzzleState:
    def __init__(self, board, x, y, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.parent = parent
    def is_goal(self):
        return self.board == goal
def print_solution(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    path.reverse()
    print("\nSolution Path:\n")
    for i, board in enumerate(path):
        print("Step:", i)
        for row in board:
            print(*row)
        print()
    print("Total Moves:", len(path) - 1)
def dfs(start, x, y):
    stack = [PuzzleState(start, x, y)]
    visited = {tuple(map(tuple, start))}
    while stack:
        current = stack.pop()
        if current.is_goal():
            print("Goal State Found")
            print_solution(current)
            return
        for dx, dy in moves:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                board = [row[:] for row in current.board]
                board[current.x][current.y], board[nx][ny] = \
                    board[nx][ny], board[current.x][current.y]
                state = tuple(map(tuple, board))
                if state not in visited:
                    visited.add(state)
                    stack.append(PuzzleState(board, nx, ny, current))
    print("No Solution Found")
# User Input
print("Enter the puzzle row by row (use 0 for blank):")
start = []
x = y = 0
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)
    for j in range(3):
        if row[j] == 0:
            x, y = i, j
dfs(start, x, y)
''',

"8_puzzle_dfs_user_def.py": r'''# 8-Puzzle Using DFS with User-Defined Initial and Goal State
N = 3
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
class PuzzleState:
    def __init__(self, board, x, y, depth=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent
def print_board(board):
    for row in board:
        print(*row)
    print()
def print_solution(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    path.reverse()
    print("\nSolution Path:\n")
    for i, board in enumerate(path):
        print("Step:", i)
        print_board(board)
    print("Total Moves:", len(path) - 1)
def dfs(start, goal, x, y):
    stack = [PuzzleState(start, x, y)]
    visited = {tuple(map(tuple, start))}
    nodes = 0

    while stack:
        current = stack.pop()
        nodes += 1
        if current.board == goal:
            print("Goal State Found!")
            print("Depth:", current.depth)
            print("Nodes Explored:", nodes)
            print_solution(current)
            return
        for dx, dy in moves:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < N and 0 <= ny < N:
                board = [row[:] for row in current.board]
                board[current.x][current.y], board[nx][ny] = \
                    board[nx][ny], board[current.x][current.y]
                state = tuple(map(tuple, board))
                if state not in visited:
                    visited.add(state)
                    stack.append(
                        PuzzleState(
                            board,
                            nx,
                            ny,
                            current.depth + 1,
                            current
                        )
                    )
    print("No Solution Found")
# User Input
print("Enter Initial State (use 0 for blank):")
start = []
x = y = 0
for i in range(N):
    row = list(map(int, input().split()))
    start.append(row)
    for j in range(N):
        if row[j] == 0:
            x, y = i, j
print("\nEnter Goal State:")
goal = []
for i in range(N):
    goal.append(list(map(int, input().split())))
print("\nInitial State:")
print_board(start)
print("Goal State:")
print_board(goal)
dfs(start, goal, x, y)
''',

"8_puzzle_dfs_optimized.py": r'''# Optimized 8-Puzzle using DFS
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
class PuzzleState:
    def __init__(self, board, x, y, depth=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent
    def is_goal(self):
        return self.board == goal
def print_solution(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    path.reverse()
    print("\nSolution Path\n")
    for step, board in enumerate(path):
        print("Step:", step)
        for row in board:
            print(*row)
        print()
    print("Total Moves:", len(path) - 1)
def dfs(start, x, y):

    stack = [PuzzleState(start, x, y)]
    visited = {tuple(map(tuple, start))}
    nodes = 0
    while stack:
        current = stack.pop()
        nodes += 1
        if current.is_goal():
            print("Goal State Found")
            print("Depth:", current.depth)
            print("Nodes Explored:", nodes)
            print_solution(current)
            return
        for dx, dy in moves:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                board = [row[:] for row in current.board]
                board[current.x][current.y], board[nx][ny] = \
                    board[nx][ny], board[current.x][current.y]
                state = tuple(map(tuple, board))
                if state not in visited:
                    visited.add(state)
                    stack.append(
                        PuzzleState(
                            board,
                            nx,
                            ny,
                            current.depth + 1,
                            current
                        )
                    )

    print("No Solution Found")
# Initial State
start = [
    [4, 2, 3],
    [1, 0, 5],
    [6, 8, 7]
]
# Blank Tile Position
x, y = 1, 1
# Run DFS
dfs(start, x, y)
''',

"8_puzzle_bfs.py": r'''# Optimal Solution of 8-Puzzle Problem Using BFS
from collections import deque
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
class PuzzleState:
    def __init__(self, board, x, y, depth=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent
def print_board(board):
    for row in board:
        print(*row)
    print()
def print_solution(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    path.reverse()
    print("\nSolution Path:\n")
    for i, board in enumerate(path):
        print("Step:", i)
        print_board(board)
    print("Total Moves:", len(path) - 1)
def bfs(start, x, y):
    queue = deque([PuzzleState(start, x, y)])
    visited = {tuple(map(tuple, start))}
    nodes = 0
    while queue:
        current = queue.popleft()
        nodes += 1
        if current.board == goal:
            print("Goal State Found!")
            print("Depth:", current.depth)
            print("Nodes Explored:", nodes)
            print_solution(current)
            return
        for dx, dy in moves:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                board = [row[:] for row in current.board]
                board[current.x][current.y], board[nx][ny] = \
                    board[nx][ny], board[current.x][current.y]
                state = tuple(map(tuple, board))
                if state not in visited:
                    visited.add(state)
                    queue.append(
                        PuzzleState(
                            board,
                            nx,
                            ny,
                            current.depth + 1,
                            current
                        )
                    )
    print("No Solution Found")
# Initial State
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]
# Blank Tile Position
x, y = 1, 1
print("Initial State:")
print_board(start)
bfs(start, x, y)
''',

"8_puzzle_bfs_input.py": r'''# 8-Puzzle Using BFS with User Input (Initial State Only)
from collections import deque
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
class PuzzleState:
    def __init__(self, board, x, y, depth=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent
def print_board(board):
    for row in board:
        print(*row)
    print()
def print_solution(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    path.reverse()
    print("\nSolution Path:\n")
    for i, board in enumerate(path):
        print("Step:", i)
        print_board(board)
    print("Total Moves:", len(path) - 1)

def bfs(start, x, y):
    queue = deque([PuzzleState(start, x, y)])
    visited = {tuple(map(tuple, start))}
    nodes = 0
    while queue:
        current = queue.popleft()
        nodes += 1
        if current.board == goal:
            print("Goal State Found!")
            print("Depth:", current.depth)
            print("Nodes Explored:", nodes)
            print_solution(current)
            return
        for dx, dy in moves:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                board = [row[:] for row in current.board]
                board[current.x][current.y], board[nx][ny] = \
                    board[nx][ny], board[current.x][current.y]
                state = tuple(map(tuple, board))
                if state not in visited:
                    visited.add(state)
                    queue.append(
                        PuzzleState(
                            board,
                            nx,
                            ny,
                            current.depth + 1,
                            current
                        )
                    )
    print("No Solution Found")
# User Input
print("Enter Initial State (3x3) row-wise (use 0 for blank):")
start = []
x = y = 0
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)
    for j in range(3):
        if row[j] == 0:
            x, y = i, j
print("\nInitial State:")
print_board(start)
# Run BFS
bfs(start, x, y)
''',

"8_puzzle_bfs_user_def.py": r'''# 8-Puzzle Using BFS with User-Defined Initial and Goal State
from collections import deque
N = 3
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
class PuzzleState:
    def __init__(self, board, x, y, depth=0, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent
def print_board(board):
    for row in board:
        print(*row)
    print()
def print_solution(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    path.reverse()
    print("\nSolution Path:\n")
    for i, board in enumerate(path):
        print("Step:", i)
        print_board(board)
    print("Total Moves:", len(path) - 1)
def bfs(start, goal, x, y):
    queue = deque([PuzzleState(start, x, y)])
    visited = {tuple(map(tuple, start))}
    nodes = 0

    while queue:
        current = queue.popleft()
        nodes += 1
        if current.board == goal:
            print("Goal State Found!")
            print("Depth:", current.depth)
            print("Nodes Explored:", nodes)
            print_solution(current)
            return
        for dx, dy in moves:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < N and 0 <= ny < N:
                board = [row[:] for row in current.board]
                board[current.x][current.y], board[nx][ny] = \
                    board[nx][ny], board[current.x][current.y]
                state = tuple(map(tuple, board))
                if state not in visited:
                    visited.add(state)
                    queue.append(
                        PuzzleState(
                            board,
                            nx,
                            ny,
                            current.depth + 1,
                            current
                        )
                    )

    print("No Solution Found")
# User Input
print("Enter Initial State (3x3) row-wise (use 0 for blank):")
start = []
x = y = 0
for i in range(N):
    row = list(map(int, input().split()))
    start.append(row)
    for j in range(N):
        if row[j] == 0:
            x, y = i, j
print("\nEnter Goal State:")
goal = []
for i in range(N):
    goal.append(list(map(int, input().split())))
print("\nInitial State:")
print_board(start)
print("Goal State:")
print_board(goal)
# Run BFS
bfs(start, goal, x, y)
''',

"a_star.py": r'''# A* Search Algorithm
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
''',

"a_star_input.py": r'''# A* with User Input (Start & Goal only)
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
# Fixed Heuristic Values
heuristic = {
    'S': 13, 'A': 12, 'B': 4,
    'C': 7, 'D': 3, 'E': 8,
    'F': 2, 'H': 4, 'I': 9, 'G': 0
}
# User Input
start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")
# Run A*
a_star(graph, heuristic, start, goal)
''',

"a_star_heuristic_input.py": r'''# A* with User Input (Start, Goal + Heuristic)
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
''',

"hill_climbing_tsp.py": r'''# Hill Climbing Algorithm for Travelling Salesman Problem(TSP)
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
''',

"minimax_tic_tac_toe.py": r'''# Minimax Algorithm (Tic-Tac-Toe)
import math
board = [" "] * 9
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
def winner(b, p):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(b[pos] == p for pos in line) for line in wins)
def draw(b):
    return " " not in b
def minimax(b, is_max, alpha, beta):
    if winner(b, "X"):
        return 1
    if winner(b, "O"):
        return -1
    if draw(b):
        return 0
    if is_max:

        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = max(
                    best,
                    minimax(b, False, alpha, beta)
                )
                b[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = min(
                    best,
                    minimax(b, True, alpha, beta)
                )
                b[i] = " "
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best
def best_move():
    move = -1
    best_score = -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
def play():
    print("Positions:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    while True:
        print_board()
        pos = int(input("Enter your move (0-8): "))
        if board[pos] != " ":
            print("Invalid Move")
            continue
        board[pos] = "O"
        if winner(board, "O"):
            print_board()
            print("You Win!")
            break
        if draw(board):
            print_board()
            print("Draw!")
            break
        ai = best_move()
        board[ai] = "X"
        print("AI chose:", ai)

        if winner(board, "X"):
            print_board()
            print("AI Wins!")
            break
        if draw(board):
            print_board()
            print("Draw!")
            break
play()
''',

"forward_backward_chaining.py": r'''# Forward Chaining and Backward Chaining
# Rules: Conditions -> Conclusion
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]
# Initial Facts
facts = {"A", "B"}
# Forward Chaining
def forward_chaining(facts):
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(c in facts for c in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("Inferred:", conclusion)
                    changed = True
    return facts
# Backward Chaining
def backward_chaining(goal):
    if goal in facts:
        return True
    for conditions, conclusion in rules:
        if conclusion == goal:
            return all(
                backward_chaining(c)
                for c in conditions
            )
    return False
# Main Program
print("Initial Facts:", facts)
print("\n--- Forward Chaining ---")
final_facts = forward_chaining(set(facts))
print("Final Facts:", final_facts)
print("\n--- Backward Chaining ---")
goal = "E"
if backward_chaining(goal):
    print("Goal", goal, "is PROVED")
else:
    print("Goal", goal, "is NOT PROVED")
''',

"unification_resolution.py": r'''# Unification and Resolution
# UNIFICATION
def unify(x, y, subst=None):
    if subst is None:
        subst = {}
    if x == y:
        return subst
    if isinstance(x, str) and x.islower():
        subst[x] = y
        return subst
    if isinstance(y, str) and y.islower():
        subst[y] = x
        return subst
    if isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for a, b in zip(x, y):
            subst = unify(a, b, subst)
            if subst is None:
                return None
        return subst
    return None
# Apply Substitution
def apply_subst(exp, subst):
    if isinstance(exp, list):
        return [apply_subst(i, subst) for i in exp]
    return subst.get(exp, exp)
# RESOLUTION
def resolve(c1, c2):
    result = []
    for l1 in c1:
        for l2 in c2:
            subst = None
            if l1[0] == "not" and l2[0] != "not":
                subst = unify(l1[1], l2)
            elif l2[0] == "not" and l1[0] != "not":
                subst = unify(l2[1], l1)
            if subst is not None:
                clause = []
                for lit in c1 + c2:
                    if lit != l1 and lit != l2:
                        clause.append(apply_subst(lit, subst))
                result.append(clause)
    return result
# Resolution Process
def resolution(kb):
    while True:
        new_clauses = []
        for i in range(len(kb)):
            for j in range(i + 1, len(kb)):
                for clause in resolve(kb[i], kb[j]):
                    if clause == []:
                        print("Contradiction Found")
                        return True
                    if clause not in kb and clause not in new_clauses:
                        new_clauses.append(clause)
        if not new_clauses:
            return False
        kb.extend(new_clauses)

# Knowledge Base
c1 = [['not', ['P', 'x']], ['Q', 'x']]
c2 = [['P', 'A']]
c3 = [['not', ['Q', 'A']]]
kb = [c1, c2, c3]
# Run Resolution
resolution(kb)
''',

"family_relationships.py": r'''# Knowledge Base for Family Relationship Reasoning
# Knowledge Base (Facts)
facts = {
    ("parent", "John", "Mary"),
    ("parent", "Mary", "Sam"),
    ("parent", "John", "Alex"),
    ("male", "John"),
    ("male", "Sam"),
    ("male", "Alex"),
    ("female", "Mary")
}
# Basic Relations
def parent(x, y):
    return ("parent", x, y) in facts
def male(x):
    return ("male", x) in facts
def female(x):
    return ("female", x) in facts
# Derived Relations
def father(x, y):
    return parent(x, y) and male(x)
def mother(x, y):
    return parent(x, y) and female(x)
def grandparent(x, z):
    for rel in facts:
        if rel[0] == "parent":
            y = rel[2]
            if parent(x, y) and parent(y, z):
                return True
    return False
def sibling(x, y):
    if x == y:
        return False
    for rel in facts:
        if rel[0] == "parent":
            p = rel[1]
            if parent(p, x) and parent(p, y):
                return True
    return False
def brother(x, y):
    return sibling(x, y) and male(x)
def sister(x, y):
    return sibling(x, y) and female(x)
# Testing
print("Father(John, Mary):", father("John", "Mary"))
print("Mother(Mary, Sam):", mother("Mary", "Sam"))
print("Grandparent(John, Sam):", grandparent("John", "Sam"))
print("Sibling(Sam, Alex):", sibling("Sam", "Alex"))
print("Brother(Alex, Sam):", brother("Alex", "Sam"))
print("Sister(Mary, Alex):", sister("Mary", "Alex"))
'''

}

for name, content in files.items():
    with open(name, "w", encoding="utf-8") as f:
        f.write(content)
print("Files generated successfully.")
