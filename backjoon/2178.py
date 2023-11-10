from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = []

    for i in range(n):
        maze.append(input())

    def bfs(grpah):
        start = (0, 0)
        visited = [[0 for i in range(m)] for i in range(n)]
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([start])
        visited[0][0] = 1
        count = 0

        while queue:
            x, y = queue.popleft()

            for dx, dy in movements:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < len(grpah) and 0 <= ny < len(grpah[0]):
                    if visited[nx][ny] == 0:
                        if grpah[nx][ny] == "1":
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append((nx, ny))

        return visited[n - 1][m - 1]

    print(bfs(maze))
