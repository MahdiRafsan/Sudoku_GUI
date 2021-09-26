def print_board(board):
    for i in range(9):
        if i != 0 and i % 3 == 0: 
                print("--------------------------")
        
        for j in range(9):
            if j != 0 and j % 3 == 0:
                print(" | ", end = " ")
                
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end = " ")
            
def is_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid_num(board, num, row, col):
    
    # check row
    for i in range(9):
        if board[row][i] == num: 
            return False
    
    # check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # check 3 X 3 square     
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False
        
    return True

def solve_sudoku(board): 
    
    row, col = is_empty(board)
    
    if row == None:
        return True

    for num in range(1, 10):
        if is_valid_num(board, num, row, col):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
        board[row][col] = 0
    
    return False

grid = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]]

if __name__ == "__main__":
    print_board(grid)
    print("\nSolving Sudoku\n")
    solve_sudoku(grid)
    print_board(grid)
