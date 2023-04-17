from itertools import product

def solution(users, emoticons):
    per = product([90, 80, 70, 60], repeat=len(emoticons))
    answer = [0, 0]
    for percent in per:
        plus = 0
        cash = 0
        for u_per, u in users:
            tot = 0
            for p in range(len(percent)):
                if 100 - u_per >= percent[p]:
                    tot += int(percent[p] * emoticons[p] // 100)
            if tot >= u:
                plus += 1
                continue
            cash += tot
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = cash
        elif answer[0] ==plus and answer[1] < cash:
            answer[1] = cash
    return answer

print(solution([[40, 10000], [25, 10000]],[7000, 9000]))