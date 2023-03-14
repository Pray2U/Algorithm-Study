import heapq


def solution(book_time):
    # 예약 리스트 정렬 및 청소시간 10분 반영 퇴실시간 적용
    for i in range(len(book_time)):
        hr = int(book_time[i][1][:2])
        mi = int(book_time[i][1][3:]) + 10
        if mi >= 60:
            mi = mi % 60
            hr += 1
        book_time[i][1] = ("%02d:%02d" % (hr, mi))
    book_time.sort()

    # 방이 몇개 필요한지 구하는 알고리즘
    rooms = []
    heapq.heappush(rooms, book_time[0][1])
    for st_time, en_time in book_time[1:]:
        ch = 0
        for ro_time in range(len(rooms)):
            if rooms[ro_time] <= st_time:
                ch = 1
                rooms[ro_time] = en_time
                break
        if ch == 0:
            heapq.heappush(rooms, en_time)
    return len(rooms)