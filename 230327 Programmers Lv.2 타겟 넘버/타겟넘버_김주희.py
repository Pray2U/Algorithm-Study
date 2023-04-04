from itertools import product


def solution(numbers, target):
    count = 0
    a = [(i, -i) for i in numbers]
    for elem in product(*a):
        b = sum(elem)
        if b == target:
            count += 1
    return count
