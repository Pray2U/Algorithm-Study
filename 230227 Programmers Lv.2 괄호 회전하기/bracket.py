def solution(s):
    count = 0
    a = ""
    for i in range(len(s)):
        if i == 0:
            a = s
        else:
            a = s[i:] + s[:i]
        stack = []
        stack.append(a[0])
        for j in range(1, len(a)):
            for b in a[j]:
                if b == '[' or b == '(' or b == '{':
                    stack.append(b)
                elif stack and b == ']' and stack[-1] == '[':
                    stack.pop()
                elif stack and b == ')' and stack[-1] == '(':
                    stack.pop()
                elif stack and b == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    break
        if len(stack) == 0:
            count += 1
    return count