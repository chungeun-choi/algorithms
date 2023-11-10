if __name__ == "__main__":
    N = int(input())
    LIST = list(map(int, input().split()))
    answer = 0
    LIST.sort()

    for index in range(N):
        if index == 0:
            answer += LIST[index]
        else:
            LIST[index] = LIST[index] + LIST[index - 1]
            answer += LIST[index]

    print(answer)
