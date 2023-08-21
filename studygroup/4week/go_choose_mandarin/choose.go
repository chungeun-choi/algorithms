package main

import (
	"fmt"
	"sort"
)

func solution(k int, tangerine []int) int {
	sizeMap := make(map[int]int)

	for _,value := range tangerine{
		if _, ok := sizeMap[value]; ok == false{
			sizeMap[value] = 1
		}else{
			sizeMap[value] +=1
		}
	}

	keys := make([]int, 0, len(sizeMap))

	for key := range sizeMap {
        keys = append(keys, key)
    }

	sort.SliceStable(keys, func(i, j int) bool{
        return sizeMap[keys[i]] > sizeMap[keys[j]]
    })
	
	var answer int = 0
	var value int = 0

	for _,key := range keys {
		if value < k {
			answer += 1
			value += sizeMap[key]
		}else{
			break
		}
	}

    return answer
}


func main() {
	testInput :=[8]int {1,3,2,5,4,5,2,3} 
	testInput2 := [8]int {1, 3, 2, 5, 4, 5, 2, 3}
	testInput3 := [8]int{1, 1, 1, 1, 2, 2, 2, 3}

	result := solution(6,testInput[:])
	fmt.Println(result)
	result2 := solution(4,testInput2[:])
	fmt.Println(result2)
	result3 := solution(4,testInput3[:])
	fmt.Println(result3)
}