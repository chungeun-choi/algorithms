package array

func solution1(num_list []int) int {

	for cnt, value := range num_list {
		if value < 0 {
			return cnt
		}
	}

	return -1
}

func solution2(num_list []int) int {
	var result int
	if len(num_list) > 10 {

		for _, value := range num_list {
			result += value
		}
	} else {
		for _, value := range num_list {
			result *= value
		}
	}

	return result
}

func solution3(num_list []int, n int) []int {
	var result []int

	result = num_list[n-1:]

	return result
}

func solution(arr []int) []int {

	for cnt, value := range arr {
		if value >= 50 && value%2 == 0 {
			arr[cnt] = value / 2
		} else if value < 50 && value%2 == 1 {
			arr[cnt] = value * 2
		} else {
			continue
		}

	}
	return arr
}
