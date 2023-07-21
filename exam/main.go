package main

import (
	"fmt"
	. "go-algorithms/exam/array"
	stack "go-algorithms/exam/stack"
)

func origin_back10808() {
	result := ImporoveSolution("testeddddfsa")
	fmt.Println(result)
}

func self_back10808() {
	result := Solution("testddddd")
	fmt.Println(result)
}


func self_programers1() {
	stack.Solution([]int{2, 1, 3, 2},2)
	stack.Solution([]int{1, 1, 9, 1, 1, 1},0)
}
func main(){
	// back10808 
	// 직접 푼 문제
	self_back10808()
	// 정답
	origin_back10808()
	
	//programers 
	self_programers1()
}