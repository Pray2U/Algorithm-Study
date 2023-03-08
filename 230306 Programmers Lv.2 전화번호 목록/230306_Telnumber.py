def solution(phone_book):
    phone_book.sort()
    key = phone_book[0]
    phone_book = phone_book[1:]
    for phone in phone_book:
        if key == phone[:len(key)]:
            return False
        key = phone
    return True