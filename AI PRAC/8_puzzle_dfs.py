# 8-Puzzle Problem using DFS
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
