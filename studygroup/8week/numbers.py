
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



def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer



if __name__ == "__main__":
    numbers= [2, 3, 3, 5]
    numbers2 = [9, 1, 5, 3, 6, 2]


    assert(solution(numbers) == [3, 5, 5, -1])
    assert(solution(numbers2) == [-1, 5, 6, 6, -1, -1])