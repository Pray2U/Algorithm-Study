from itertools import combinations as cm
from collections import defaultdict


def solution(info, query):
    dic = defaultdict(list)
    for i in range(5):
        print(list(cm(range(4),i)))
    # for each_info in info:
    #     each_info = each_info.split()
    #     condition, score = each_info[:-1], int(each_info[-1])
        # 조합을 어떻게 찾지..?
        # Example
        # java backend junior pizza 150     1
        # java    -    junior pizza 150     2
        # java backend    -   pizza 150     3
        # java backend junior   -   150     4
        #   -  backend junior pizza 150     5
        #   -     -    junior pizza 150     6
        #   -  backend    -   pizza 150     7
        #   -  backend junior   -   150     8
        # java    -       -   pizza 150     9
        # java    -    junior   -   150     10
        # java backend    -     -   150     11
        # java    -       -     -   150     12
        #   -  backend    -     -   150     13
        #   -     -    junior   -   150     14
        #   -     -       -   pizza 150     15
        #   -     -       -     -   150     16

        # binary search library : bisect
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query)) # [1,1,1,1,2,4]
