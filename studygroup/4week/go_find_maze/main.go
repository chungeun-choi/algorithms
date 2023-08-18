package gofindmaze

import (
	"fmt"
)

type Position struct {
	x int
	y int

}

func main() {
	queue := make(chan Position, 10000)
	value := &Position{
		x: 123,
		y: 22,
	}
	queue <- *value

	//var result Position

	
	fmt.Println(<- queue)
	
}