package main

import (
	"fmt"
	"unicode/utf8"
)

type Pos struct {
	x int
	y int
}

func bfs(start *Pos, end *Pos, maps []string) int {
	queue := make(chan *Pos, 10000)
	var moving = [4]Pos{
		{x: -1, y: 0},
		{x: 1, y: 0},
		{x: 0, y: -1},
		{x: 0, y: 1},
	}
	width := utf8.RuneCountInString(maps[0])
	hight := len(maps)

	visited := make([][]int, hight)
	for i := range visited {
		visited[i] = make([]int, width)
	}

	queue <- start
	visited[start.x][start.y] = 1

	for position := range queue {
		x := position.x
		y := position.y

		for _, value := range moving {
			nx := x + value.x
			ny := y + value.y

			if 0 <= nx && nx < hight && 0 <= ny && ny < width {
				if visited[nx][ny] == 0 {
					if x_value := maps[nx]; x_value[ny] != 'X' {
						positions := &Pos{
							x: nx,
							y: ny,
						}
						if positions.x == end.x && positions.y == end.y {
							return visited[x][y]
						} else {
							visited[nx][ny] = visited[x][y] + 1
							queue <- positions
						}
					}

				}
			}
		}

	}
	return -1
}

func solution(maps []string) int {
	// 시작 위치, 레버 위치, 탈출 위치 찾기

	// bfs를 통해 시작위치에서 레버위치까지 거리
	// 레버위치에서 탈출 위치까지의 거리 찾기
	// 거리에서 return 하는 값이 없을 경우 탈출 경로가 없다 판단하여 return -1
	test_start := &Pos{
		x: 0,
		y: 0,
	}
	test_lever := &Pos{
		x: 0,
		y: 4,
	}
	result := bfs(test_start, test_lever, maps)
	fmt.Println(result)
	return 0
}

func main() {
	testInput := [5]string{"SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"}

	solution(testInput[:])

}
