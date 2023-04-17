'''
from collections import deque

def solution(stones, k):
    deq = deque()
    answer = 200000000
    for idx, val in enumerate(stones):
        if len(deq) >= k:
            deq.popleft()
        while (deq):
            if deq[-1] >= val:
                break
            deq.pop()

        deq.append(val)
        if idx > k-1:
            if answer > deq[0]:
                answer= deq[0]
    return answer
'''


def solution(stones, k):
    li = sorted(set(stones))
    if len(li) == 1:
        return li[0]
    answer = li[len(li) // 2]
    while len(li) > 2:
        mididx = len(li) // 2 + 1
        mid = li[mididx]
        cnt = 0
        pm = True

        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt == k:
                    pm = False
                    break
            else:
                cnt = 0

        if pm:
            answer = mid
            li = li[1:]
        else:
            li = li[:-1]

    return answer


'''
def solution(stones, k):
    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        pm = True

        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt == k:
                    pm = False
                    break
            else:
                cnt = 0

        if pm:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
'''

#print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3))
print(solution([1, 2, 3, 4, 5],	2))