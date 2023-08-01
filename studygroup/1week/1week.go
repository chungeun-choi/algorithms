package main

import (
	"fmt"
)

func Solution(N,M int)int{
	X := 0
	count := 1
	for {
		X = (X+M)%N 
		if X == 0{
			break
		}else{
			count++
		}
	}
	return count
}
	


func main() {
	result := Solution(10,4)
	fmt.Println(result)
}