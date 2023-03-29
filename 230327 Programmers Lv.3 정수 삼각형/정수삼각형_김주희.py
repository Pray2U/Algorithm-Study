def solution(triangle):
    answer = triangle[:]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if i == 0:
                answer[i+1][i] += answer[i][i]
                answer[i+1][i+1] += answer[i][i]
            elif i > 1 and j == 0:
                answer[i][j] += answer[i-1][j]
            elif i > 1 and j == i:
                answer[i][j] += answer[i-1][j-1]
            elif i > 1:
                answer[i][j] += max(answer[i-1][j-1], answer[i-1][j])

    return max(answer[-1])