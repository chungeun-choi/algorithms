from collections import deque
# 직사각형인데 문제 똑바로 안 읽고 정사각형인 줄 알고 풀었다가 틀림....
def solution(maps):
    def bfs(start,end):
        visited = [[0]*wid for i in range(hei)]
        queue = deque([start])
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        visited[start[0]][start[1]] = 1

        while queue:
            x,y = queue.popleft()
            for cnt in range(0,4):
                nx = x + dx[cnt]
                ny = y + dy[cnt]
                
                if nx < 0 or ny < 0 or nx >= hei or ny >= wid:
                    continue
                if maps[nx][ny] == "X" or visited[nx][ny] != 0:
                    continue
                visited[nx][ny] = visited[x][y] +1
                queue.append((nx,ny))
        return  visited[end[0]][end[1]] -1
    
    hei = len(maps)
    wid = len(maps[0])

    for i in range(hei):
        for j in range(wid):
            if maps[i][j] == "S":s_pos = (i,j)
            elif maps[i][j] == "L" : l_pos = (i,j)
            elif maps[i][j] == "E" : e_pos = (i,j)
    
    l_distacne = bfs(s_pos,l_pos)
    if l_distacne == -1:
        return -1
    e_distance = bfs(l_pos,e_pos)
    if e_distance == -1:
        return -1

    return l_distacne + e_distance






if __name__ == "__main__":
    test_input = {
        "maps":["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
    }

    test_input2 = {
        "maps":["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
    }

    test_input3 = {
        "maps":["SELOX", "XXXXO", "OOOOO", "OXXXX", "OOOOO"]
    }

    test_input4 = {
        "maps":["SXXOX", "EXXXL", "OOXOO", "OXXXX", "OOOOO"]
    }

    test_input5 = {
        "maps": ["SLXOX", "EXXXO", "OOOOO", "OXXXX", "OOOOO"]
    }
    assert(solution(**test_input)==16)
    assert(solution(**test_input2)== -1)
    assert(solution(**test_input3)==3)
    assert(solution(**test_input4)==-1)
    assert(solution(**test_input5)==3)

