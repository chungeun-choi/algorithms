from collections import deque


def solution(maps):
    def bfs(st, en) -> int:
        vis = [[0 for i in range(wid)] for j in range(hei)]
        Q = deque()
        Q.append(st)
        vis[st[0]][st[1]] = 1
        while Q:
            x, y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= hei or ny >= wid:
                    continue
                if maps[nx][ny] == "X" or vis[nx][ny] != 0:
                    continue
                vis[nx][ny] = vis[x][y] + 1
                Q.append((nx, ny))
        return vis[en[0]][en[1]] - 1

    hei = len(maps)
    wid = len(maps[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(hei):
        for j in range(wid):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)

    time1 = bfs(start, lever)
    if time1 == -1:
        return -1
    time2 = bfs(lever, end)
    if time2 == -1:
        return -1
    return time1 + time2
