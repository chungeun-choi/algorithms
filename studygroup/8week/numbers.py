
# solved task in first time
def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):
        count =i
        while count <len(numbers)-1:
            count +=1
            if numbers[i] < numbers[count]:
                answer.append(numbers[count])
                break
        else:
            answer.append(-1)
    return answer



if __name__ == "__main__":
    numbers= [2, 3, 3, 5]
    numbers2 = [9, 1, 5, 3, 6, 2]


    assert(solution(numbers) == [3, 5, 5, -1])
    assert(solution(numbers2) == [-1, 5, 6, 6, -1, -1])