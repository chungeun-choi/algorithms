from collections import deque

def dfs(start,end,maps):
    # 'end'에 도착 시 거리를 저장 해두기 위한 리스트
    distance_list = []
    # 테이블의 가로세로 길이
    width = len(maps[0])
    hight = len(maps)
    # 방문 여부 확인 테이블
    initializer = float('inf')
    visited = [[initializer]*width for _ in range(hight)]
    # stack 생성
    stack = deque([(start,0)])
    # start 위치의 값 1로 변경
    visited[start[0]][start[1]] = 1
    # 이동 경로
    moving = [(-1,0),(1,0),(0,-1),(0,1)]

    while stack:
        # stack pop - stack에 담긴 위치 값과 시간 값 
        pos,time = stack.pop()
        x,y =  pos
        
        if pos == end :
            distance_list.append(time)
            continue
        
        for dx,dy in moving:
            nx,ny = x +dx , y+dy

            temp_time = time + 1
            if 0 <= nx < hight and 0 <= ny < width and maps[nx][ny] != 'X' and temp_time < visited[nx][ny]:
                visited[nx][ny] = temp_time
                # 조합 결과 콜 스택 전달
                stack.append([(nx,ny), temp_time])
    
    if len(distance_list) == 0:
        return -1
    
    else:
        return min(distance_list)


def solution(maps):
    answer = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":s_pos = (i,j)
            elif maps[i][j] == "L" : l_pos = (i,j)
            elif maps[i][j] == "E" : e_pos = (i,j)
    
    

    l_time = dfs(s_pos,l_pos,maps)
    if l_time == -1:
        return -1
    e_time = dfs(l_pos,e_pos,maps)
    if e_time == -1:
        return -1
    
    return l_time+e_time



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