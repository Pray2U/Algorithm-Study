import math


def primenumber(x):
    for i in range(2, x):	# 2부터 x-1까지의 모든 숫자
        if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
            return False
    return True

# 소수 판별
def primenumber_2(x):
    for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
        if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True

def primenumber_3(x):
    n = 1000	# 2부터 1000까지 모든 수에 대하여 소수를 찾을 것이다.
    array = [True for i in range(n + 1)] # 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
        if array[i] == True:	# i가 소수인 경우 i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
                
    #모든 소수 출력
    for i in range(2, n + 1):
        if array[i]:
            print(i, end = ' ')