def solution(phone_book):
    dic = {}
    phone_book.sort(key=len)

    for value in phone_book:
        i = 0
        while len(phone_book[0])+i <= len(value):
            key = value[:len(phone_book[0])+i]
            if key in dic:
                return False
            i += 1
        dic[value] = 1
            
    return True

phone_book = ["119", "97674223", "97674223524421"]

print(solution(phone_book))


def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book)]:
            return False
        
        
    return answer

def solution(phone_book): 
    for i in range(len(phone_book)): 
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]: 
                return False
            
    return True

def solution(phone_book):
    hash = {}
    
    for phone_num in phone_book:
        hash[phone_num] = 1
    
    for phone_num in phone_book:
        tmp = ""
        for x in phone_num:
            tmp += x
            if tmp in hash and tmp != phone_num:
                return False
    return True