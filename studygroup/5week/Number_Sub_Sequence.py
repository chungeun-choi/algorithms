from itertools import permutations


def solution(elements):
    answer = 0
    leng_elements = len(elements)

    for count in range(1, leng_elements + 1):
        if count == 1:
            answer += len(set(elements))
            continue
        if count == leng_elements:
            answer += leng_elements
            continue
        else:
            check_list = set()
            for count2 in range(0, leng_elements):
                range_value = count + count2
                if range_value > leng_elements:
                    value = sum(elements[count2:leng_elements]) + sum(
                        elements[: abs(leng_elements - (range_value))]
                    )
                    check_list.add(value)
                check_list.add(sum(elements[count2:range_value]))
            answer += len(check_list)

    return answer


if __name__ == "__main__":
    elements = [7, 9, 1, 1, 4]

    assert solution(elements=elements) == 18
