from collections import deque


def solution(maps):
    q = deque()
    q.append((0, 0))

    n = len(maps) - 1
    m = len(maps[0]) - 1

    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]

    while q:
        a, b = q.popleft()

        for i in range(len(x)):
            dx = a + x[i]
            dy = b + y[i]
            if dx < 0 or dy < 0 or dx > n or dy > m:  #맵밖으로나가면
                continue
            if maps[dx][dy] == 1:
                maps[dx][dy] = maps[a][b] + 1
                q.append((dx, dy))
    if maps[n][m] == 1:
        return -1
    else:
        return maps[n][m]
