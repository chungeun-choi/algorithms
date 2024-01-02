# def solution(topping):
#     answer = 0
#     pivot = len(topping)//2
#
#     for pivot in range(0,len(topping)):
#         left = len(set(topping[0:pivot]))
#         right = len(set(topping[pivot:]))
#
#         if left == right:
#             answer +=1
#
#     return answer
def solution(topping):
    answer = 0
    #length = len(topping)

    forward = set()
    backward = {}
    for i in topping:
        backward[str(i)] = backward.get(str(i), 0)
        backward[str(i)] += 1
    for i in topping:
        forward.add(i)
        backward[str(i)] -= 1
        if backward[str(i)] == 0:
            del backward[str(i)]
        if len(forward) == len(backward.keys()):
            answer += 1
    return answer

if __name__ == '__main__':
    test_case = {
        "topping":[1, 2, 1, 3, 1, 4, 1, 2]
    }
    test_case2 = {
        "topping":[2,3,1,4,3,2]
    }

    assert solution(test_case["topping"]) == 2