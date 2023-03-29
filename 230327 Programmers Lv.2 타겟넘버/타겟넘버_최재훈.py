def solution(numbers, target):
    # 순서 유지 필요.
    # numbers의 각 원소를 +, - 2개의 부호로 바꾸어서 총 2개의 트리를 생성
    # 트리를 돌면서 합을 구함. 총합이 타겟넘버와 같으면 1을 반환.
    def recursiveTree(numbers, sum, target):
        if numbers == []:
            if sum==target: return 1
            else:   return 0
        # print(f"numbers[0] : {numbers[0]}")
        # print(f"numbers[1:] : {numbers[1:]}")
        return recursiveTree(numbers[1:], sum + numbers[0], target) + recursiveTree(numbers[1:], sum - numbers[0], target)
    return recursiveTree(numbers, 0, target)

print(solution([1,1,1,1,1],3)) # 5
print(solution([4,1,2,1],4)) # 2