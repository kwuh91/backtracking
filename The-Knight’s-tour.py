# Time Complexity: O(8^(N^2))
# Auxiliary Space: O(N^2)

def printSolution(board: [[int]]) -> None:
    for i in board:
        for j in i:
            print(f"{j}", end="  ") if j >= 10 else print(f"{j}", end="   ")
        print(f"")


def isSafe(x: int, y: int, board: [[int]], n: int) -> bool:
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def solveKT(n: int) -> None:
    board = [[-1 for _ in range(n)] for _ in range(n)]

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0

    pos = 1

    if solveKTUtil(n, board, 0, 0, move_x, move_y, pos):
        printSolution(board)
    else:
        print(f"There is no solution")


def solveKTUtil(n: int, board: [[int]], curr_x: int, curr_y: int, move_x: [int], move_y: [int], pos: int) -> bool:
    if pos == n * n:
        return True

    for i in range(n):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(new_x, new_y, board, n):
            board[new_x][new_y] = pos
            if solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos + 1):
                return True
            board[new_x][new_y] = -1
    return False


if __name__ == "__main__":
    solveKT(8)
