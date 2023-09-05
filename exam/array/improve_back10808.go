package array

import (
	"bufio"
	"fmt"
	"strings"
)

func ImporoveSolution(s string) (result string) {
	count := make([]int, 26)

	for _, c := range s {
		char := rune(c) - rune('a')
		count[char]++
	}

	for _, i := range count {
		result += fmt.Sprintf("%d", i)
	}

	result = strings.TrimSpace(result)

	return
}

func Scan(rd *bufio.Reader) string {
	str, _ := rd.ReadString('\n')
	str = strings.TrimSpace(str)

	return str

}
