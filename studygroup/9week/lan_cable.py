import sys

K, N = map(int, sys.stdin.readline().split())
cable_list = [int(sys.stdin.readline()) for i in range(K)]


half_value = max(cable_list)
answer = []


def caclulator(half):
    count = 0
    for i in cable_list:
        count += i // half

    return count


def binary_search(start, end):

    if end < start:
        return

    half = (end + start) // 2
    value = caclulator(half)

    if value >= N:
        answer.append(half)
        binary_search(half + 1, end)
    else:
        binary_search(start, half - 1)


binary_search(0, half_value * 2)

print(max(answer))
