package main

import (
	"container/list"
	"fmt"
)

type Stack struct {
	v *list.List
}

func NewStack() *Stack {
	return &Stack{list.New()}
}

func (q *Stack) Push(v interface{}) {
	q.v.PushBack(v)
}

func (q *Stack) Pop() interface{} {
	back := q.v.Back()
	if back == nil {
		return nil
	}

	return q.v.Remove(back)
}

func check(strList string) bool {
	stack := NewStack()

	for _, runeValue := range strList {
		if runeValue == '[' || runeValue == '(' || runeValue == '{' {
			stack.Push(runeValue)
		} else {
			if stack.v.Len() == 0 {
				return false
			}
			x := stack.Pop()
			if runeValue == ']' && x != '[' {
				return false
			} else if runeValue == ')' && x != '(' {
				return false
			} else if runeValue == '}' && x != '{' {
				return false
			}

		}
	}
	if stack.v.Len() > 0 {
		return false
	}

	return true
}

func solution(s string) int {
	answer := 0
	for cnt, _ := range s {
		u := s[:cnt]
		v := s[cnt:]

		if check(v + u) {
			answer += 1
		}
	}

	return answer
}

func main() {

	result := solution("}]()[{")
	fmt.Print(result)

}
