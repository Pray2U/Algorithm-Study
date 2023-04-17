def solution(stones, k):
    answer = 0
    for length in range(0, len(stones)-k):
        temp = stones[length:length+k]
        #print(f'temp : {stones[length:length+k]} / answer : {answer}')
        min_val = min(temp)
        answer = max(answer, min_val)
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) #3