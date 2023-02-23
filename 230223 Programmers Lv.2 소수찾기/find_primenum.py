from itertools import permutations


def solution(numbers):
    answer = 0 
    numbers = list(numbers)
    num = []
    int_num = []
    for i in range(1,len(numbers)+1):
        num += list(permutations(numbers,i))
    for nu in num:
        int_num+= [int(''.join(nu))]
    num = set(int_num)
    for i in num:
        if i < 2:
            continue
        else:
            is_pri = 0
            for pri in range(2,int(i**0.5)+1):
                if i % pri == 0:
                    is_pri = 1
                    break
            if is_pri == 0:
                answer += 1
    return answer
