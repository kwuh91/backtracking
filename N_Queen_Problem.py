# board must be N * N

def solveNQueen(board: [[int]], col: int = 0) -> bool:
    def boardprint(board: [[int]]) -> None:
        for i in board:
            for j in i:
                if j == 1:
                    print(f"Q", end="  ")
                else:
                    print(f".", end="  ")
            print(f"")

    if len(board) != len(board[0]):
        raise Exception("Invalid dimensions")
    n = len(board)
    if col >= n:
        boardprint(board)
        return True

    def isSafe(board: [[int]], row: int, col: int, n: int) -> bool:
        # there in no need in checking the column and up/down-right diagonals
        # because we go from left to right in this algorithm

        # check row
        if 1 in board[row]: return False
        # check diagonal up-left
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        # check diagonal down-left
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    for row in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            if solveNQueen(board, col + 1):
                return True
            board[row][col] = 0

    return False


if __name__ == '__main__':

    print(f"Enter N - amount of queens on a N * N board: ")
    N: int = int(input())
    myboard = [[0 for _ in range(N)] for _ in range(N)]
    if not solveNQueen(myboard):
        print(f"there is no solution")
