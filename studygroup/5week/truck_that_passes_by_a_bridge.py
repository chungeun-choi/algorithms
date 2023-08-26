from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    way = deque([])

    while queue:
        pass

    return answer


if __name__ == '__main__':
    test_input = {
        "bridge_length":2,
        "weight":10,
        "truck_weights":[7,4,5,6,],
    }

    assert(solution(**test_input)==8)