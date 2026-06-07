# 8-Puzzle Using DFS with User Input
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
