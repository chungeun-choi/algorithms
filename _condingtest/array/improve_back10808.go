package array

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func ImporoveSolution(s string) (result string) {
	count := make([]int,26)

	for _,c := range(s){
		char := rune(c) - rune('a')
		count[char]++
	}

	for _, i := range count {
		result += fmt.Sprintf("%d",i)
	}

	result = strings.TrimSpace(result)

	return
}


func scan (rd *bufio.Reader) string {
	str, _:= rd.ReadString('\n')
	str = strings.TrimSpace(str)

	return str

} 


func main() {
	rd := bufio.NewReader(os.Stdin)
	wr := bufio.NewWriter(os.Stdout)

	word:= scan(rd)

	_,_ = wr.WriteString(ImporoveSolution(word))
	_ = wr.Flush()
}