from itertools import permutations

def isPrime(num):
    # 숫자가 2보다 작으면 무조건 소수가 아니기에 False를 리턴
    # (for문 돌리는데 범위를 맞추기 어려워 미리 걸러냄)
    # 2부터 자기 자신의 제곱근까지 나누어 떨어지지 않을 경우 소수로 판별

    if num < 2:
        return False
    for i in range(2,int(num**0.5+1)):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numList = []
    
    for i in range(1,len(numbers)+1):
        numList += list(permutations(list(numbers),i))
    # permutations(순열)을 사용하여 각 숫자들로 만들 수 있는 경우의 수를 다 구한다.

    numValue = [int("".join(x)) for x in numList]
    # join()을 통하여 전 단계에서 구한 경우의 숫자들을 결합 후 int로 형 변환 

    for num in set(numValue):
        if isPrime(num):
            answer += 1
    # set()을 통해 중복된 숫자들을 삭제한 뒤 해당 숫자가 소수인지 판별

    return answer

numbers = "011"
print(solution(numbers))

# 핵심 알고리즘?
# 1. 문자열을 리스트로 변환
# 2. 숫자 리스트를 통해 만들 수 있는 모든 숫자 조합을 구함(순열)
# 3. 모든 숫자 조합에서 중복 제거
# 4. 소수 판별








































from itertools import permutations
import math

def is_Prime(num):
    if num < 2:
        return False
    else:
        ran = int(math.sqrt(num))+1
        for i in range(2,ran):
            if num % i == 0:
                return False    
        return True
    
def solution(numbers):
    answer = 0
    Nums = [n for n in numbers]
    numList = []
    
    for i in range(1,len(Nums)+1):
        numList += list(permutations(Nums,i))
    LIST = [int(("").join(x)) for x in numList]
    
    
    for x in list(set(LIST)):
        if is_Prime(x):
            answer += 1
    
    return answer