def solution(n):
    answer = []
    board = [4,1,2]
    w, t = 0, 0 # w가 몫, t가 나머지
    
    while n>0:
        w = n//3
        t = n%3
        if w>=3:
            answer.append(t)
            n = w
            continue

        if t == 0:
            w -= 1
            answer.append(board[t])
            if w != 0:
                answer.append(w)
        else:
            answer.append(board[t])
            if w != 0:
                answer.append(w)
        break
    return int(''.join(map(str, answer[::-1])))

print(solution(11)) #42

# def solution(n):
#     arr = [4,1,2]
#     result = ""
#     while n > 0:
#         result += str(arr[n%3])
#         if n%3 == 0:
#             n = n//3 -1
#         else:
#             n = n//3

#     return result[::-1]