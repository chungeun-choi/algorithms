package stack

import (
	"fmt"
)

type Stack struct {
	arrayList []int
}

func NewStack() *Stack {
	return &Stack{}
}

func (s *Stack) Push(value int) {
	s.arrayList = append(s.arrayList, value)
}

func (s *Stack) Pop() int {
	result := s.arrayList[len(s.arrayList)-1]
	s.arrayList = s.arrayList[:len(s.arrayList)-1]
	return result
}

func (s *Stack) GetObjectALl() {
	for _, value := range s.arrayList {
		fmt.Println(value)
	}
}
