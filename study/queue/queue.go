package queue

import (
	"fmt"
)

type Queue struct {
	list []int
}

func NewQueue() QueueInterface {
	return &Queue{}
}

func (q *Queue) Push(value int) {

	q.list = append(q.list, value)
	fmt.Printf("Queue size: %d \n", len(q.list))
}

func (q *Queue) Pop() int {

	result := q.list[0]
	q.list = q.list[1:]
	fmt.Printf("Queue size: %d \n", len(q.list))
	return result
}

func (q *Queue) GetAllObject() {
	for _, value := range q.list {
		fmt.Println(value)
	}
}
