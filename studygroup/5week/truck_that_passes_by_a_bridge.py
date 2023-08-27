'''
    제한 조건
    bridge_length는 1 이상 10,000 이하입니다.
    weight는 1 이상 10,000 이하입니다.
    truck_weights의 길이는 1 이상 10,000 이하입니다.
    모든 트럭의 무게는 1 이상 weight 이하입니다.
'''

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    way = deque([])
    truck_weight = 0

    while queue:
        
        if len(way) !=0:
            _,value = way.popleft()
            answer += value
            continue
        else:
            truck_weight = queue.popleft()
            way.append([truck_weight,bridge_length])
            if truck_weight + queue[0] <= weight:
                way.append([queue.popleft(),1])

    return answer


if __name__ == '__main__':
    test_input = {
        "bridge_length":2,
        "weight":10,
        "truck_weights":[7,4,5,6,],
    }

    assert(solution(**test_input)==8)