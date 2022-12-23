def solve_sudoku(board):
    # kontrollo nese nje vlere eshte e vlefshme ne nje qelize te caktuar
    def is_valid(i, j, value):
        # row constraints
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

    # graph coloring + BFS 
    def solve():
        # te gjitha qelizat (qe kemi mi eksploru)
        queue = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

        # perserite deri sa queue te jet empty (te jen mbushur te gjitha)
        while queue:
            # merr qelizen tjeter nga queue
            i, j = queue.pop(0)

            # kontrollo te gjitha vlerat per nje qelize
            for value in range(1, 10):
                if is_valid(i, j, value):
                    board[i][j] = value
                    if solve():
                        return True
                    board[i][j] = 0

        # nese queue eshte empty dhe te gjitha cells jane vizituar, sudoku eshte i zgjidhur
        return not queue

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