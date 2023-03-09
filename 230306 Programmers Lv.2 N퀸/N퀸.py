from itertools import permutations
from functools import reduce


def solution(n):
    global answer
    answer = 0
    
    def check(idx,col):
        global answer
        n=len(col)
        if promising(idx,col) :
            if idx==n-1:
                answer += 1
            else :
                for j in range(n):
                    col[idx+1] = j
                    check(idx+1,col)
    
    def promising(idx,col):
        for k in range(idx):
            if (col[idx]==col[k]) or (abs(col[idx]-col[k])==idx-k) :
                return False
        return True

    for i in range(n):
        col = [i] + [0]*(n-1)
        check(0,col)
    return answer


# 개 미쳤다...ㄷㄷ
def nQueen(n):
    return reduce(lambda s,q: len(set({i-v:i+v for i,v in enumerate(q)}.values()))==n and s+1 or s, permutations(range(n)), 0)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nQueen(8))
print(solution(8))

