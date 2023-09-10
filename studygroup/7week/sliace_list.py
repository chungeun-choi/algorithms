def solution(n, left, right):
    answer = []
    list_value = [i for i in range(1,n+1)]
    answer = answer+list_value
    for i in range(1,n):
        value = [ i+1 for j in range(i+1)]+list_value[i+1:]
        answer = answer + value
    return answer[left:right+1]


if __name__ == "__main__":
    test_input_1= {
        "n":3,
        "left":2,
        "right":5
    }

    test_input_2 = {
        "n":4,
        "left":7,
        "right":14
    }

    assert(solution(**test_input_1)==[3,2,2,3])
    assert(solution(**test_input_2)==[4,3,3,3,4,4,4,4])