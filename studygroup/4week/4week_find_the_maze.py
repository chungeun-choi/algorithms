def dfs(start,end,maps):
    width = len(maps[0])
    hight = len(maps)
    visited = [[0]*width for i in range(hight)]
    moving = [(-1,0),(1,0),(0,-1),(0,1)]
    queue = [start]
    visited[start[0]][start[1]] = 1

    while queue:
        x,y = queue.pop()
        
        for dx,dy in moving:
            nx, ny = x+dx,y+dy

            if 0 <= nx < hight and 0 <= ny < width:
                if maps[nx][ny] != "X" and visited[nx][ny] ==0:
                    if (nx,ny) == end:
                        return visited[x][y]
                    visited[nx][ny] = visited[x][y] +1
                    queue.append((nx,ny))
                
    return -1


from collections import deque

def bfs(start,end,maps):
    width = len(maps[0])
    hight = len(maps)
    visited = [[0]*width for i in range(hight)]
    moving = [(-1,0),(1,0),(0,-1),(0,1)]
    queue = deque([start])
    visited[start[0]][start[1]] = 1

    while queue:
        x,y = queue.popleft()
        
        for dx,dy in moving:
            nx, ny = x+dx,y+dy

            if 0 <= nx < hight and 0 <= ny < width:
                if maps[nx][ny] != "X" and visited[nx][ny] ==0:
                    if (nx,ny) == end:
                        return visited[x][y]
                    visited[nx][ny] = visited[x][y] +1
                    queue.append((nx,ny))
                
    return -1

# 직사각형인데 문제 똑바로 안 읽고 정사각형인 줄 알고 풀었다가 틀림....
def solution(maps):

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":s_pos = (i,j)
            elif maps[i][j] == "L" : l_pos = (i,j)
            elif maps[i][j] == "E" : e_pos = (i,j)
    
    l_distacne = dfs(s_pos,l_pos,maps)
    if l_distacne == -1:
        return -1
    e_distance = dfs(l_pos,e_pos,maps)
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

