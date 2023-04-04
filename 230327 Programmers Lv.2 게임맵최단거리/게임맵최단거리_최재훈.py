from collections import deque


def solution(maps):
    move = [[-1,1,0,0], [0,0,-1,1]]
    M, N = len(maps[0]), len(maps)
    
    queue=deque([(0,0)])
    
    while queue:
        # print(f'queue : {queue}')
        x,y = queue.popleft()
        # print(f'x, y / queue : {x}, {y} / {queue}')
        if (x,y) == (N-1,M-1):
            return maps[x][y]

        for i in range(4):
            nx = x + move[0][i]
            ny = y + move[1][i]
            # print(f'nx, ny : {nx}, {ny}')
            
            if 0<=nx<N and 0<=ny<M:
                if maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx,ny))
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) #11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) #-1