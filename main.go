package main

import (
	"fmt"

	. "github.com/cucuridas/go-algorithms/_condingtest/array"
	. "github.com/cucuridas/go-algorithms/array/practiceCode"

	. "github.com/cucuridas/go-algorithms/linkedlist"
	. "github.com/cucuridas/go-algorithms/stack"
)



func main(){
	//배열 자료구조 확인
	//array()
	//improveArray()
	//back10808()
	//quetion()
	//linkedList()

	stack()
}


func array() {
	array := []int{1,2,3,4,5}

	insertArray := Insert(2,27,array)

	fmt.Println(insertArray)

	deleteArray := Delete(4,insertArray)

	fmt.Println(deleteArray)
	
}

func improveArray() {
	array := []int{1,2,3,4,5}

	insertArray := ImproveInsert(2,27,array)

	fmt.Println(insertArray)


	deleteArray := ImproveDelete(2,array)

	fmt.Println(deleteArray)

}

func back10808() {
	testValue := "abcder"
	Solution(testValue)
}


func quetion(){
	arrya := []int{1,33,12,66,34}
	result := QSolution(arrya,5)

	fmt.Printf("%d",result)
}


func linkedList() {
	linkd := NewLinkedList(1233)

	linkd.InsertNext(2434)
	linkd.InsertNext(544)
	linkd.InsertNext(55621)


	linkd.GetAllNodes()

	linkd.DeleteLast(nil)

	linkd.GetAllNodes()


	linkd.DeleteIndex(2)

	linkd.GetAllNodes()

	linkd.InsertIndex(1,659)

	linkd.GetAllNodes()


	_,value := linkd.GetIndexNode(2)

	fmt.Println(value)

	linkd.DeleteNode(value)


	linkd.GetAllNodes()

	
}


func stack(){
	stack := NewStack()

	stack.Push(123)
	stack.Push(33)
	stack.Push(6642)
	stack.Push(1233)

	stack.GetObjectALl()


	result := stack.Pop()
	fmt.Printf("After Pop %d \n",result)
	stack.GetObjectALl()

}