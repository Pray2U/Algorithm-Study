def solution(book_time):
    a = []
    b = []
    t1 = []
    t2 = []
    time = sorted(book_time, key = lambda x : x[0]) # 입실 시간 기준 정렬
    for i in time:
        b.append(i[0])
        a.append(i[1])
    for j in range(len(time)):
        c = b[j].split(':')
        d = a[j].split(':')
        t1.append(int(c[0]) * 60 + int(c[1]))
        t2.append(int(d[0]) * 60 + int(d[1]) + 10)
    room = []
    for e in range(len(t1)):
        if not room:
            room.append(t2[e])
        elif t1[e] < room[-1]: # 퇴실 시간 > 다음 입실 시간 -> 방 추가
            room.append(t2[e])
            room.sort(reverse = True)
        else: # 퇴실 시간 새로 업데이트
            room.pop()
            room.append(t2[e])
            room.sort(reverse = True)
    return len(room)