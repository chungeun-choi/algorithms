from typing import List, Tuple
from collections import deque


class Solution:
    def bfs(
        self, start: Tuple[int], grid: List[List[str]], visited: List[List[str]]
    ) -> Tuple[List[List[str]], int]:
        value = 1
        position = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([start])
        visited[start[0]][start[1]] = 1
        while queue:
            y, x = queue.popleft()
            for dx, dy in position:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                    continue
                else:
                    if visited[ny][nx] == 0 and grid[ny][nx] == "1":
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                    else:
                        continue
        return (visited, value)

    def numIslands(self, grid: List[List[str]]) -> int:
        # start 지점 찾기 (visited 테이블에서 방문하지 않아야함, grid의 값이 0이 아니여야 함)
        # queue에 넣고 bfs 탐색
        # queue가 종료 시 추가로 start 지점 찾기

        result = 0
        visited = [[0] * len(grid[0]) for i in range(len(grid))]

        start_list = []

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    start_list.append((y, x))

        for i in start_list:
            if visited[i[0]][i[1]] == 1:
                continue

            visited, value = self.bfs(start=i, grid=grid, visited=visited)
            result += value

        return result


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert Solution().numIslands(grid=grid) == 1
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert Solution().numIslands(grid=grid2) == 3
