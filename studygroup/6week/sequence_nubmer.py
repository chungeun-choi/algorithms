def solution(elements):
    answer = 0
    length = len(elements)
    sums = []

    # 초기값 설정
    sums.extend(elements)

    for n in range(length + 1):
        if n == 0 or n == 1:
            continue
        for i in range(length):
            m = (i + n - 1) % length  # 이어붙일 한칸짜리 인덱스를 조정하는 작업
            sums.append(sums[(n - 2) * length + i] + sums[m])  # 이전사이클 값 + 이어붙일 한칸짜리 값

    answer = len(list(set(sums)))
    return answer


if __name__ == "__main__":
    assert solution([7, 9, 1, 1, 4]) == 18
