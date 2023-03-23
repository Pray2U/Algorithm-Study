def solution(s):
    answer = 0
    first = ""
    cnt = 0
    
    for x in s:
        if cnt == 0:
            answer += 1
            first = x
        if first == x:
            cnt += 1
        else:
            cnt -= 1
            
    return answer