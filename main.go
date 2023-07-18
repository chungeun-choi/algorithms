package main

import (
	"fmt"

	. "github.com/cucuridas/go-algorithms/array/practiceCode"
	. "github.com/cucuridas/go-algorithms/condingtest/array"
)



func main(){
	//배열 자료구조 확인
	//array()
	//improveArray()
	//back10808()
	quetion()
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