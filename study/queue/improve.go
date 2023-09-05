package queue

import (
	"fmt"
)

type ImproveQueue struct {
	list   []int
	tail   int
	header int
}

func NewImproveQueue(size int) QueueInterface {
	return &ImproveQueue{
		list:   make([]int, size),
		tail:   0,
		header: 0,
	}
}

func (q *ImproveQueue) Push(value int) {

	if q.tail > len(q.list)-1 {
		q.tail = 0
	}

	q.list[q.tail] = value
	q.tail++
	fmt.Printf("Queue size: %d \n", len(q.list))
}

func (q *ImproveQueue) Pop() int {

	if q.header > len(q.list)-1 {
		q.header = 0
	}

	result := q.list[q.header]
	q.header++

	return result
}

func (q *ImproveQueue) GetAllObject() {
	for _, value := range q.list {
		if value == 0 {
			continue
		}
		fmt.Println(value)
	}
}
