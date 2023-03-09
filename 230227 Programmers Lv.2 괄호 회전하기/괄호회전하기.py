from collections import deque

def solution(s):
    answer = 0
    queue = deque(s)

    for shfit in range(len(s)):
        if checking(queue):
            answer += 1
        queue.append(queue.popleft())
    
    return answer
            
def checking(str):
    dic = { "[":"]", "{":"}", "(":")"}
    stack = []
    for value in str:
        if value in ["[", "{", "("]:
            stack.append(value)
        else:
            if stack and value == dic[stack[-1]]:
                stack.pop(-1)
            else:
                return False
    if stack:
        return False
    return True 

































from collections import deque

def solution(s):
    answer = 0
    dq = deque(s)
    
    for i in range(len(s)):
        if checking(dq):
            answer += 1
        dq.append(dq.popleft())
    
    return answer

def checking(s):
    stack = []
    dic = {
        '[':']',
        '(':')',
        '{':'}',
    }

    for x in s:
        if x == "[" or x == "(" or x == "{":
            stack.append(x)
        else:
            if stack and dic[stack[-1]] == x:
                stack.pop(-1)
            else:
                return False
    
    if stack:
        return False
    else:
        return True
