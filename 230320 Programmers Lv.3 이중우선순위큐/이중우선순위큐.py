def solution(operations):
    answer = []
    for cmd in operations:
        if cmd=="D 1":
            if len(answer) == 0:
                continue
            else:
                del answer[answer.index(max(answer))]
        elif cmd=="D -1":
            if len(answer) == 0:
                continue
            else:
                del answer[answer.index(min(answer))]
        else:
            num = int(cmd[2:])
            answer.append(num)
    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]