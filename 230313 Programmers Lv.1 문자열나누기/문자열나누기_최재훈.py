# Solution 01

def solution(s):
    answer, bucket = 0, [0, 0] # bucket[0] = 첫글자의 개수, bucket[1] = 첫글자와 다른 나머지 글자의 개수
    idx = 0
    for index, elem in enumerate(s):
        if elem == s[idx]:
            bucket[0] += 1
        else:
            bucket[1] += 1
        
        if bucket[0] == bucket[1]:
            answer += 1
            idx = index +1
            bucket[0], bucket[1] = 0, 0
        else:
            if index+1 >= len(s):
                answer += 1
                #print(f'{bucket} {answer} {index} {elem}')
                break
        #print(f'{bucket} {answer} {index} {elem}')
    return answer

print(solution("banana")) #3
print(solution("abracadabra")) #6
print(solution("aaabbaccccabba")) #3