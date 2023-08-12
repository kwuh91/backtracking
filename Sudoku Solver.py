# Time complexity: O(9(N*N))
# Space Complexity: O(N*N)

def solveSudoku(board: [[int]]) -> None:
    n = len(board)
    moves = [x for x in range(1, 9 + 1)]
    if solveSudokuUtil(board, n, moves, 0, 0):
        printSolution(board)
    else:
        print(f"There is no solution")


def solveSudokuUtil(board: [[int]], n: int, moves: [int], row: int, col: int) -> bool:
    if row == n - 1 and col == n:
        return True

    if col == n:
        row += 1
        col = 0

    if board[row][col] != 0:
        return solveSudokuUtil(board, n, moves, row, col + 1)

    for i in moves:
        if isValid(board, n, row, col, i):
            board[row][col] = i
            if solveSudokuUtil(board, n, moves, row, col + 1):
                return True
            board[row][col] = 0

    return False


def isValid(board: [[int]], n: int, row: int, col: int, num: int) -> bool:
    for i in range(n):
        if board[row][i] == num: return False
        if board[i][col] == num: return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False
    return True


def printSolution(board: [[int]]) -> None:
    for i in board:
        for j in i:
            print(f"{j}",end="  ")
        print(f"")


if __name__ == "__main__":
    myboard = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
               [5, 2, 0, 0, 0, 0, 0, 0, 0],
               [0, 8, 7, 0, 0, 0, 0, 3, 1],
               [0, 0, 3, 0, 1, 0, 0, 8, 0],
               [9, 0, 0, 8, 6, 3, 0, 0, 5],
               [0, 5, 0, 0, 9, 0, 6, 0, 0],
               [1, 3, 0, 0, 0, 0, 2, 5, 0],
               [0, 0, 0, 0, 0, 0, 0, 7, 4],
               [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    solveSudoku(myboard)
