from collections import deque

def solution(queue1, queue2):
    answer = -2

    que1 = deque(queue1)
    que2 = deque(queue2)

    sum_que1 = sum(que1)
    sum_que2 = sum(que2)

    for i in range(len(que1)*3):
        if sum_que1 == sum_que2:
            return i
        else:
            if sum_que1 > sum_que2:
                value = que1.popleft()
                que2.append(value)
                sum_que1 -= value
                sum_que2 += value
            else :
                value = que2.popleft()
                que1.append(value)
                sum_que2 -= value
                sum_que1 += value
    
    answer = -1

    return answer




if __name__ == "__main__":
    test_input = {
        "queue1":[3, 2, 7, 2],
        "queue2":[4, 6, 5, 1]
    }
    test_input2 = {
        "queue1":[1, 2, 1, 2],
        "queue2":[1, 10, 1, 2]
    }

    test_input3 = {
        "queue1":[1, 1]	,
        "queue2":[1, 5]
    }

    assert(solution(**test_input) == 2)
    assert(solution(**test_input2) == 7)
    assert(solution(**test_input3)== -1)