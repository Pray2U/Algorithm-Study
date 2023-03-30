from itertools import product
def solution(numbers, target):
    answer = 0
    tot = 0
    if sum(numbers) < target:
        return 0
    numlist = list(product([1,-1],repeat=len(numbers)))
    numli =  [[x*y for x,y in zip(numbers,i)]for i in numlist]
    for num in numli:
        if sum(num)==target:
            answer += 1
    return answer