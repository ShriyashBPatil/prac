# Optimized 8-Puzzle using DFS
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
