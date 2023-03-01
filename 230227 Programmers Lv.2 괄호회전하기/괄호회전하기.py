def solution(s):
    def isRight(target):
        stack = []
        for idx, elem in enumerate(target):
            if elem in ('[', '(', '{'):
                stack.append(elem)
            else:
                if not stack: return False
                x = stack.pop()
                if elem == ']' and x != '[':
                    return False
                elif elem == '}' and x != '{':
                    return False
                elif elem== ')' and x != '(':
                    return False
        if stack: return False
        return True
                
        
    answer = 0
    tmp = s+s
    for start in range(0, len(s)):
        # print(f"{start}번째 문자열 : {tmp[start:start+len(s)]}")
        if isRight(tmp[start:start+len(s)]):
            answer += 1
    return answer

print(solution("[](){}")) #3
print(solution("}]()[{")) #2
print(solution("[)(]")) #0
print(solution("}}}")) #0