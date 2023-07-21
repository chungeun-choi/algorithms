package linkedlist

import (
	"fmt"
)

type LinkedList struct {
	Header *Node
	Tail *Node
	Count int 
}


func NewLinkedList(value int ) *LinkedList{

	node := NewNode(value)

	return &LinkedList{
		Header: node,
		Tail: node,
		Count: 1,
	}
}

func (ll *LinkedList)InsertNext(value int){
	newNode := NewNode(value)

	newNode.prev = ll.Tail
	ll.Tail.next = newNode
	
	ll.Tail= newNode

	ll.Count++

}

func (ll *LinkedList)InsertIndex(index int,value int){
	start := ll.Header
	newNode := NewNode(value)

	for cnt := 1;cnt <= ll.Count ; cnt ++ {
		if cnt == index {
			fmt.Printf("Insert index %d object \n",index)
			newNode.prev = start
			newNode.next = start.next

			start.next = newNode
			newNode.next.prev = newNode

			ll.Count++
			break

		}else{
			start = start.next
		}

	}

}

func (ll *LinkedList)DeleteLast(value interface{}){
	if value == nil {
		fmt.Println("Delete last object")
		ll.Tail.prev.next = nil 
		ll.Tail = ll.Tail.prev

		ll.Count-- 

	}
}

func (ll *LinkedList)DeleteIndex(index int){
	start := ll.Header
	for cnt := 1;cnt <= ll.Count ; cnt ++ {
		if cnt == index {
			fmt.Printf("Delete index %d object \n",index)

			start.prev.next = start.next
			start.next.prev = start.prev

			ll.Count--
			break
		}else{
			start = start.next
		}

	}

}


func (ll *LinkedList)DeleteNode(node *Node){
	if ll.Header == node {
		ll.Header = node.next
		node.next.prev= nil 
	}else if ll.Tail == node {
		ll.Tail = node.prev
		node.prev.next = nil
	}else {	
		node.prev = node.next
		node.next.prev = node.prev
		ll.Count--
	}

}


func (ll *LinkedList)GetAllNodes(){
	result := ll.Header

	for cnt := 0;cnt < ll.Count ; cnt ++ {
		fmt.Println(result.value)

		result = result.next
	}
}


func (ll *LinkedList)GetIndexNode(index int) (error, *Node){
	result := ll.Header

	for cnt := 1 ; cnt <= ll.Count ; cnt++ {
		if cnt == index {
			fmt.Printf("%d that you want obejct \n",result.value)
			return nil,result
		}else {
			result = result.next
		}
	}
	return fmt.Errorf("No object of index"),nil

}