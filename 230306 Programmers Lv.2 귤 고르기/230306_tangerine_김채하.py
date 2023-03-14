from collections import Counter


def solution(k, tangerine):
    if k == 1: return 1
    if k == len(tangerine): return len(set(tangerine))

    dic = dict(Counter(tangerine).most_common())

    tot = 0
    ind = 0
    for val in dic.values():
        tot += val
        ind += 1
        if tot >= k:
            return ind
