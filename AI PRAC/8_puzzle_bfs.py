# Optimal Solution of 8-Puzzle Problem Using BFS
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
