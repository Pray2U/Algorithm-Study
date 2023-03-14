# 1차시도 : set copy를 사용한 이중 for문 순회
# def solution(phone_book):
#     targets = set(phone_book)
#     for elem in targets:
#         tmp = targets.copy()
#         tmp.remove(elem)
#         for target in tmp:
#             if target in elem:
#                 return False
#     return True

# 2차시도 : Hashing을 이용한 이중 for문 순회
def solution(phone_book):
    board = { number:1 for number in phone_book }
    
    for numbers in phone_book:
        prefix = ""
        for number in numbers:
            prefix += number
            if prefix in board and prefix != numbers:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))  # false
print(solution(["123","456","789"]))                # true
print(solution(["12","123","1235","567","88"]))     # false