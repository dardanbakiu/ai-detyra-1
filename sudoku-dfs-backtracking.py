def solve_sudoku(board):
    # gjej qelizen fqinje te thate
    def find_empty_cell():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    # shiko nese vlera eshte e sakt ne nje qelize te caktuar
    def is_valid(i, j, value):
        # Check row constraints
        if value in board[i]:
            return False

        # column constraints
        for k in range(9):
            if board[k][j] == value:
                return False

        # block constraints
        block_i = i // 3
        block_j = j // 3
        for k in range(3):
            for l in range(3):
                if board[3 * block_i + k][3 * block_j + l] == value:
                    return False

        return True

    # graph coloring + DFS + backtracking
    def solve():
        empty_cell = find_empty_cell()
        if empty_cell is None:
            return True

        i, j = empty_cell
        for value in range(1, 10):
            if is_valid(i, j, value):
                board[i][j] = value
                if solve():
                    return True
                board[i][j] = 0

        return False

    solve()

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(puzzle)

for row in puzzle:
    print(row)