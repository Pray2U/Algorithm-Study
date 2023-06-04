def solution(s, bomb):
    # s = str(input())
    # bomb = str(input())

    stack = []
    for elem in s:
        stack.append(elem)
        if "".join(stack[-len(bomb):])== bomb:
            for _ in range(len(bomb)):
                stack.pop()
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')

print(solution("mirkovC4nizCC44", "C4")) #mirkovniz
print(solution("12ab112ab2ab", "12ab")) #FRULA