from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    dic = {}

    for i in range(len(info)):
        a = info[i].split()
        info_key = a[:-1]  # 조건들
        info_score = int(a[-1])  # 점수

        for j in range(5):
            for b in combinations(info_key, j):
                c = ''.join(b)
                if c not in dic:
                    dic[c] = [info_score]
                else:
                    dic[c].append(info_score)

    for k in dic:
        dic[k].sort()

    for d in query:
        z = d.split(' ')
        q_key = z[:-1]
        q_score = int(z[-1])

        while 'and' in q_key:
            q_key.remove('and')
        while '-' in q_key:
            q_key.remove('-')

        q_key = ''.join(q_key)

        if q_key in dic:  # dic에 있으면 score 저장
            score = dic[q_key]
            if score:
                zz = bisect_left(score, q_score)

                answer.append(len(score) - zz)
        else:
            answer.append(0)
    return answer
