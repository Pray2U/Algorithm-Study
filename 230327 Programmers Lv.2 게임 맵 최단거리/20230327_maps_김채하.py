from collections import deque


def solution(maps):
    x = 0
    y = 0
    dis = 1
    que = deque()
    que.append([x, y, dis])
    while que:
        x, y, dis = que.popleft()
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return dis

        if maps[x][y] == 0:
            continue

        maps[x][y] = 0

        dic = {'r': (0, 1), 'd': (1, 0), 'l': (0, -1), 'u': (-1, 0)}

        if x == 0:
            del (dic['u'])
        if x == len(maps) - 1:
            del (dic['d'])
        if y == 0:
            del (dic['l'])
        if y == len(maps[0]) - 1:
            del (dic['r'])

        maps[x][y] = 0
        for key, val in dic.items():
            if maps[x + val[0]][y + val[1]] == 1:
                que.append([x + val[0], y + val[1], dis + 1])

    return -1
