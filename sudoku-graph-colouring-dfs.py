def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # kontrollo nese numri eshte ne ate rresht
        for i in range(9):
            if board[row][i] == num:
                return False

        # kontrollo nese numri eshte ne ate kolone
        for i in range(9):
            if board[i][col] == num:
                return False

        # kontrolo nese numri eshte ne boxin 3x3
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def assign_color(board, row, col, colors):
        # cakto ngjyren per nje qelize
        for color in colors:
            if is_valid(board, row, col, color):
                board[row][col] = color
                # # provo me caktu ngjyren per te tjera qelizat
                if assign_color(board, row, col + 1, colors):
                    return True
                # nese nuk esht mire reseto edhe provo prap
                board[row][col] = 0
        # nese asnje nuk punon kthe false 
        return False

    # start with a list of all possible colors (numbers from 1 to 9)
    colors = list(range(1, 10))
    # assign colors to the cells using graph coloring
    assign_color(board, 0, 0, colors)


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

print(solve_sudoku(puzzle))