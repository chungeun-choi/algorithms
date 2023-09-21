from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heappush(h, e)
        if len(h) > k:
            n -= heappop(h)
        if n < 0:
            return i
    return len(enemy)

    


if __name__ == "__main__":
    test_case1 = {
        "n":7,
        "k":3,
        "enemy":	[4, 2, 4, 5, 3, 3, 1]	
    }

    test_case2 = {
        "n":2,
        "k":4,
        "enemy":[3, 3, 3, 3]
    }

    test_case3 = {
        "n":15,
        "k":1,
        "enemy":[3, 2, 5, 5,7]
    }
    assert(solution(**test_case1)==5)
    assert(solution(**test_case2)==4)
    print(solution(**test_case3))