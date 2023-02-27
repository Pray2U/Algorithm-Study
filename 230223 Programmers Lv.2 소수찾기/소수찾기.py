from itertools import permutations


# Programmers 58.3/100
def solution(numbers):
    # 1차 시도
    comb = set()
    for i in range(1, len(numbers)+1):
        comb |= set(list(map(int, map("".join, permutations(list(numbers), i)))))
    comb -= set([0,1])
    for i in range(2, int(max(comb) ** 0.5) + 1):
        comb -= set(range(i * 2, max(comb) + 1, i))
    return len(sorted(list(comb)))

# Programmers 100/100
def solution_2(numbers):
    # 2차 시도
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    target = set()

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            if is_prime(int("".join(j))):
                target.add(int("".join(j)))
    return len(sorted(list(target)))

print(solution("9939")) # 소수가 없는 케이스가 들어올 경우 max()에서 에러가 남!
print(solution_2("9939"))