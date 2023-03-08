from collections import Counter
def solution(k, tangerine):
    b = []
    count = 0
    answer = 0
    if k == 1:
        return 1
    else:
        a = Counter(tangerine)
        for value in a.values():
            b.append(value)
        b.sort(reverse = True)
        for i in b:
            if answer >= k:
                break
            else:
                answer += i
                count += 1
    return count