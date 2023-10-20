def is_safe(board, row, col, n):
    # Kiểm tra hàng ngang bên trái
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Kiểm tra đường chéo trên bên trái
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Kiểm tra đường chéo dưới bên trái
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("Không tìm thấy giải pháp.")
        return
    print_board(board)

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0
    
    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))

# Sử dụng hàm để giải bài toán 8 Quân Hậu
solve_n_queens(8)
