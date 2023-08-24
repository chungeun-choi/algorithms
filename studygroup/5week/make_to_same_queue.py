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