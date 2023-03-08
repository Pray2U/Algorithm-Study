import heapq as h


def solution(book_time):
    answer = 1
    book_time_sort = sorted(book_time)
    book_time_list = [(int(elem_x[:2])*60 + int(elem_x[3:]), int(elem_y[:2])*60 + int(elem_y[3:])) for elem_x, elem_y in book_time_sort]
    
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