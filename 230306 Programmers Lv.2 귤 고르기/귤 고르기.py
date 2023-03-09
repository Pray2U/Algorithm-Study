from collections import Counter
def solution(k, tangerine):
    cntList = []
    
    dic = dict(Counter(tangerine))

    for key, value in dic.items():
        cntList.append(value)
    
    cntList.sort(reverse=True)
    del_cnt = len(tangerine) - k

    while cntList[-1] <= del_cnt:
        del_cnt -= cntList.pop()
    
    return len(cntList)


k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k,tangerine))