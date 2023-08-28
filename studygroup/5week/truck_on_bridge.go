package main

import (
	"container/list"
	"fmt"
)

type Queue struct {
  v *list.List
}

func NewQueue() *Queue {
  return &Queue{list.New()}
}

func (q *Queue) Push(v interface{}) {
  q.v.PushBack(v)
}

func (q *Queue) Pop() interface{} {
  front := q.v.Front()
  if front == nil {
    return nil
  }

  return q.v.Remove(front)
}


func solution(bridge_length int, weight int, truck_weights []int) int {
    wating := NewQueue()
	bridge := NewQueue()
	bridgeWeight := 0 
	time := 0
	//truck 무게가 담긴 queue 생성
	for _,value := range truck_weights{
		wating.Push(value)
	}

	for i:= 0; i<bridge_length; i++ {
		bridge.Push(0)
	}


	for bridgeWeight > 0 || wating.v.Len()> 0{
		removeTruck := bridge.Pop()
		bridgeWeight = bridgeWeight - removeTruck.(int)
		

		if wating.v.Len() >0 && wating.v.Front().Value.(int) + bridgeWeight <= weight{
			truck:= wating.Pop()
			bridgeWeight = bridgeWeight+ truck.(int)
			bridge.Push(truck)
		}else {
			bridge.Push(0)
		}

		time += 1
	}
	
	return time
}


func main() {
	bridge_length := 2
	weight := 10
	truck_weights := []int{7, 4, 5, 6,}
	result := solution(bridge_length,weight,truck_weights)

	fmt.Print(result)
}