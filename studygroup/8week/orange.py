from collections import Counter

def solution(k, tangerine):
    answer = 0

    counter_value = Counter(tangerine)
    
    for _,value in sorted(counter_value.items(),key= lambda x: x[1],reverse=True):
        if k <= 0:
            break
        k -= value
        answer+=1
    
    return answer


if __name__ == "__main__":
    test_case1 = {
        "k":6,
        "tangerine":[1, 3, 2, 5, 4, 5, 2, 3],
    }

    test_case2 = {
        "k":4,
        "tangerine":[1, 3, 2, 5, 4, 5, 2, 3],
    }

    test_case3 = {
        "k":2,
        "tangerine":[1, 1, 1, 1, 2, 2, 2, 3],
    }

    assert(solution(**test_case1)==3)
    assert(solution(**test_case2)==2)
    assert(solution(**test_case3)==1)