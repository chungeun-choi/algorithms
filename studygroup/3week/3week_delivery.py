def solution(cap, n, deliveries, pickups):
    answer = 0
    start_size = n
    return_size = n

    for i in range(n,0,-1):
        box = cap
        if deliveries[i] == 0 and pickups[i] == 0:
            continue
        else:
            answer += i+1
            start_size -= deliveries[i]
            return_size -= pickups[i]

            
    
    return answer

def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    d = 0
    p = 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2
    return answer
    


if __name__ == "__main__":
    test_input = {
        "cap":4,
        "n":5,
        "deliveries":[1, 0, 3, 1, 2],
        "pickups":[0, 3, 0, 4, 0]
    }

    test_input2 = {
        "cap":2,
        "n":7,
        "deliveries":[1, 0, 2, 0, 1, 0, 2],
        "pickups":[0, 2, 0, 1, 0, 2, 0]
    }

    assert(solution(**test_input)==16)
    assert(solution(**test_input2)==30)