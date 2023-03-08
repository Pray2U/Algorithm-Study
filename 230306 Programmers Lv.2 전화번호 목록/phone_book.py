def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            break
        a = phone_book[i]
        b = phone_book[i+1]
        if a in b and b.index(a) == 0:
            return False
    return True