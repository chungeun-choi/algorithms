package array

// 근데 최악의 수에서 이게 완벽할까?....
// 어차피 최악의 수라면 O(n)만큼 돌아야할 듯 크게 의미를 두지않도록 하자
func ImproveInsert(index, value int, array []int) []int {
	array = append(array, array[len(array)-1])

	for cnt := len(array) - 3; cnt >= index; cnt-- {
		array[cnt+1] = array[cnt]
	}

	array[index] = value

	return array

}

func ImproveDelete(index int, array []int) []int {
	for cnt := index; cnt < len(array)-1; cnt++ {
		array[cnt] = array[cnt+1]
	}

	return array[:len(array)-1]

}
