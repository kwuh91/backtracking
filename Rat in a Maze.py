# Time Complexity: O(2^(n^2))
# Auxiliary Space: O(n^2)

def solveRatInAMaze(board: [[int]], n: int = None) -> None:
    if n is None: n = len(board)
    board[0][0] = 2
    if solveRatInAMazeUtil(n, board, 0, 0):
        printSolution(board)
    else:
        print(f"Solution doesn't exist")


def solveRatInAMazeUtil(n: int, board: [[int]], x: int, y: int) -> bool:
    if board[n - 1][n - 1] == 2:
        return True

    if isSafe(n, board, x + 1, y):
        board[x + 1][y] = 2
        if solveRatInAMazeUtil(n, board, x + 1, y):
            return True
        board[x + 1][y] = 1

    if isSafe(n, board, x, y + 1):
        board[x][y + 1] = 2
        if solveRatInAMazeUtil(n, board, x, y + 1):
            return True
        board[x][y + 1] = 1

    return False


def isSafe(n: int, board: [[int]], x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n and board[x][y] == 1


def printSolution(board: [[int]]) -> None:
    for i in board:
        for j in i:
            if j == 2:
                print(f"1", end="  ")
            elif j == 1:
                print(f"0", end="  ")
            else:
                print(f"0", end="  ")
        print(f"")


if __name__ == "__main__":
    # maze1 = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    # solveRatInAMaze(maze1)
    maze2 = [[1, 1, 1, 1, 1, 0],
             [1, 0, 1, 1, 1, 1],
             [1, 1, 1, 0, 1, 1],
             [1, 1, 1, 0, 0, 0],
             [1, 0, 1, 1, 1, 1],
             [1, 0, 0, 1, 1, 1]]

    solveRatInAMaze(maze2)
