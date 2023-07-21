package stack

import (
	"sort"
)

func Solution(priorities []int, location int) int {
    queue := append([]int(nil), priorities...)
    ordered := append([]int(nil), priorities...)
    sort.Sort(sort.Reverse(sort.IntSlice(ordered)))

    cnt := 1
    pos := location
    target := priorities[location]
    // 우선순위에 의해서 가장 먼저 나오는 요소가 기존 슬라이스에
    // 몇번째 위치하고 있는지
    for _, next := range ordered {
        idx := 0

        for i, q := range queue {
            if q == next {
                idx = i
                break
            }
        }
        // 찾고자 하는 location의 값인지 체크
        // next의 값이 target과 같거나, idx의 값과 location의 값이 같을 경우
        if next == target && idx == pos {
            return cnt
        }
        // 내가 찾고자하는 target의 위치 정보를 갱신
        if pos > idx {
            pos -= idx + 1
        } else {
            pos += len(queue) - idx - 1
        }


        cnt++
        queue = append(queue[idx+1:], queue[:idx]...)
    }

    return cnt
}
