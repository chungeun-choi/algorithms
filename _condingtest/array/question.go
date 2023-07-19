package array

func QSolution(s []int,len int) int {
	freq := make([]int, 101)

	for _,value := range(s){
		if freq[100 - value] == 1{
			return 1
		}else {
			freq[value] = 1
		}
	}
	return 0 
}