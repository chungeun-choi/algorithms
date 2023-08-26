def solution(arr):
    if len(arr)==1:
        return [-1]
    else:
        min_num=min(arr)
        del arr[arr.index(min_num)]
        return arr


if __name__ == "__main__":
    test_input = {
        "arr" : [4,3,2,1],

    }

    test_input2 = {
        "arr" : [10],
        
    }

    assert(solution(**test_input)==[4,3,2])
    assert(solution(**test_input2)==[-1])