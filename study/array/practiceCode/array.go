package array

func Add(value int, array []int) {
	array = append(array, value)
}

// 값 복사 때문에 무조건적으로 지금 O(n) 만큼 돌리게 됨
// index 기준으로 값 참조해서 변경할 경우 O((index/len(array))*n)으로 판단되는데...
func Insert(index, value int, array []int) []int {
	returnArray := make([]int, len(array)+1)
	for cnt, value := range array {
		if cnt >= index {
			returnArray[cnt+1] = array[cnt]
		} else {
			returnArray[cnt] = value
		}
	}

	returnArray[index] = value

	return returnArray
}

func Delete(index int, array []int) []int {
	var cntIndex int = 0
	returnArray := make([]int, len(array)-1)
	for cnt := 0; cnt < len(array); cnt++ {
		if cnt == index {
			continue
		}

		returnArray[cntIndex] = array[cnt]
		cntIndex++

	}
	return returnArray
}
