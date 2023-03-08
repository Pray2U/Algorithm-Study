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