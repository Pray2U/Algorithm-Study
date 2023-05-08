def solution(n):
    arr = [4,1,2]
    result = ""
    while n > 0:
        result += str(arr[n%3])
        if n%3 == 0:
            n = n//3 -1
        else:
            n = n//3
    
    return result[::-1]