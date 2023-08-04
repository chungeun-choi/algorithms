from collections import Counter

def solution(N, stages):
    answer = []
    peoples = len(stages)
    info_stay_stages = Counter(stages)

    for i in range(1,N+1):
        value = info_stay_stages[i]
        if value == 0 :
            answer.append((i,0))
        else :
            failure = value/peoples
            peoples = peoples - value
            answer.append((i,failure))

    answer.sort(key=lambda x : x[1],reverse=True)
    answer = list(map(lambda x: x[0],answer))

    return answer




if __name__== "__main__":
    # programmers - 실패율 [https://school.programmers.co.kr/learn/courses/30/lessons/42889]
    test1_input = {
        "N": 5,
        "stages": [2, 1, 2, 6, 2, 4, 3, 3]	
    }

    test1_input2 = {
        "N":4,
        "stages":[4,4,4,4,4]
    }
    assert(solution(**test1_input)==[3,4,2,1,5])
    assert(solution(**test1_input2)==[4,1,2,3])