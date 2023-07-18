package main

import (
	"fmt"

	. "github.com/cucuridas/go-algorithms/array"
)



func main(){
	//array()
	improveArray()
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