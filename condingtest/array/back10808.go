package array

import (
	"fmt"
	"strings"
)

const startAlpha = 97


func Solution(s string) {
	//returnArray := make([]int, 26)
	for cnt := startAlpha ; cnt <= startAlpha + 26 ;cnt ++ {
		fmt.Print(strings.Count(s,string(cnt)))
	}
}

