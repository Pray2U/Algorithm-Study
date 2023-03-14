from collections import Counter


def solution(k, tangerine):
    answer, bucket = 0, dict(Counter(tangerine).most_common())
    for idx in bucket:
        if k<=0:
            return answer
        k -= bucket[idx]
        answer += 1
    return answer


print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3])) # 	3
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3])) #   2
print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3])) # 	1