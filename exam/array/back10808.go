package array

import (
	"bufio"
	"fmt"
	"strings"
)

const startAlpha = 97


func Solution(s string) string {
	//returnArray := make([]int, 26)
	var result string 
	for cnt := startAlpha ; cnt <= startAlpha + 25 ;cnt ++ {
		result += fmt.Sprintf("%d",strings.Count(s,string(cnt)))
	}
	result = strings.TrimSpace(result)
	return result
}

func scan10808(rd *bufio.Reader) string {
	str, _ := rd.ReadString('\n') // 여기서 text는 마지막에 줄바꿈 문자를 포함하므로
	str = strings.TrimSpace(str)  // 줄바꿈 문자를 제거해야 함
	return str
}

// func main() {
// 	rd := bufio.NewReader(os.Stdin)
// 	wr := bufio.NewWriter(os.Stdout)

// 	word := scan10808(rd)


// 	_,_ = wr.WriteString(Solution(word))
// 	_ = wr.Flush()
// }