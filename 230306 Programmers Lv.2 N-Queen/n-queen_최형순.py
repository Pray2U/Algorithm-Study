def solution(n):
    answer = 0
    global board
    board = [-1]*n
    for row in range(n):
        board[0] = row
        answer += nqueen(1,n)

    return answer

def nqueen(col,n):
    if col == n:
        return 1
    
    result = 0

    for row in range(n):
        check = True
        for colNum in range(col):
            if row == board[colNum] or abs(board[colNum]-row) == abs(colNum-col):
                check = False
                break
        if check:
            board[col] = row
            result += nqueen(col+1,n)
            
    return result

n = 4
print(solution(n))































# def solution(n):
#     answer = 0
#     global board
#     board = [-1]*n
#     for i in range(n):
#         board[0] = i
#         answer += nqueen(1,n)
#     return answer

# def nqueen(x,n):
#     if x == n:
#         return 1
#     else:
#         result = 0
#         for y in range(n):
#             check = True
#             for x2 in range(x):
#                 if y == board[x2] or abs(y-board[x2]) == abs(x-x2):
#                     check = False
#                     break
#             if check:
#                 board[x] = y
#                 result += nqueen(x+1,n)
                
#         return result 