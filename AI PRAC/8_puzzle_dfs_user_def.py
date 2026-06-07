# 8-Puzzle Using DFS with User-Defined Initial and Goal State
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
