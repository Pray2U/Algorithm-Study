import heapq as h


def solution(book_time):
    def convertExpression(x1,x2):
        return (int(x1[:2])*60 + int(x1[3:]), int(x2[:2])*60 + int(x2[3:]))
    
    answer = 1
    book_time_sort = sorted(book_time)
    book_time_list = [convertExpression(elem[0], elem[1]) for elem in book_time_sort]
    
    heap = []
    for elem_start, elem_end in book_time_list:
        if not heap:
            h.heappush(heap, elem_end)
            continue
        if heap[0] <= elem_start:
            h.heappop(heap)
        else:
            answer += 1
        h.heappush(heap, elem_end+10)
    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3