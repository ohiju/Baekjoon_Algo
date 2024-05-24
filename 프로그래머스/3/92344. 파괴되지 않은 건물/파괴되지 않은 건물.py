def solution(board, skill):
    ans = 0
    n = len(board)
    m = len(board[0])
    new_board = [[0]*m for _ in range(n)]
    
    for sk in skill:
        t, r1, c1, r2, c2, degree = sk
        
        if t == 1:
            new_board[r1][c1] -= degree
            if r2 < n - 1:
                new_board[r2 + 1][c1] += degree
            if c2 < m - 1:
                new_board[r1][c2 + 1] += degree
            if r2 < n - 1 and c2 < m - 1:
                new_board[r2 + 1][c2 + 1] -= degree
        
        elif t == 2:
            new_board[r1][c1] += degree
            if r2 < n - 1:
                new_board[r2 + 1][c1] -= degree
            if c2 < m - 1:
                new_board[r1][c2 + 1] -= degree
            if r2 < n - 1 and c2 < m - 1:
                new_board[r2 + 1][c2 + 1] += degree
        
    cnt = 0
    for i in range(n):
        for j in range(m-1):
            new_board[i][j+1] += new_board[i][j]
    
    for j in range(m):
        for i in range(n-1):
            new_board[i+1][j] += new_board[i][j]
            
    for i in range(n):
        for j in range(m):
            board[i][j] += new_board[i][j]
            if board[i][j] > 0:
                ans += 1
    
    return ans