from collections import deque
if __name__ == "__main__":
    n = int(input())
    map = []
    sector = []
    visited = [[0 for i in range(n)] for i in range(n)]
    movements = [(-1,0),(1,0),(0,-1),(0,1)]

    for i in range(n):
        map.append(input())

    def bfs(graph,start):
        queue = deque([start])
        visited[start[0]][start[1]] = 1
        count = 1 

        while queue:
            x,y = queue.popleft()

            for dx,dy in movements:
                nx = x + dx 
                ny = y + dy

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) :
                    if visited[nx][ny] == 0 :
                        if graph[nx][ny] == '1':
                            count +=1
                            visited[nx][ny] = 1
                            queue.append((nx,ny))
        
        return count
                            
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and map[i][j] == "1":
                sector.append(bfs(map,(i,j)))
        
    sector.sort()
    print(len(sector))
    for i in sector:
        print(i)

