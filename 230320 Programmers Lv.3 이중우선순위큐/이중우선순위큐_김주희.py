def solution(operations):
    answer = []
    for a in operations:
        answer.sort()
        b, c = a.split()[0], int(a.split()[1])
        if b == 'I':
            answer.append(c)
        elif b == 'D' and c == -1:
            if answer != []:
                answer.pop(0)
        elif b == 'D' and c == 1:
            if answer != []:
                answer.pop(-1)
    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]