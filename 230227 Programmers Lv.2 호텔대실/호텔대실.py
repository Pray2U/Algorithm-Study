from heapq import heappush, heappop
def solution(book_time):
    answer = 0
    minTime = []
    heap = []

    for time in book_time:
        start = int(time[0][:2])*60 + int(time[0][3:])
        end = int(time[1][:2])*60 + int(time[1][3:])
        minTime.append([start,end])

    minTime.sort()
    for start, end in minTime:
        if not heap:
            heappush(heap,end+10)
            answer += 1
        else:
            if heap[0] <= start:
                heappop(heap)
            else:
                answer += 1
            heappush(heap,end+10)
            
    return answer

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))