from collections import deque
# 어떠한 삽으로 5개의 광물을 채굴했을 때 피로도 계산하는 함수
def check_tired(pick,divide_list):
    tired = 0 
    mineral_weight = {
        "diamond":0,
        "iron":1,
        "stone":2
    }
    
    for divide_object in divide_list :
        weitght = mineral_weight[divide_object]
        if pick <=weitght:
            tired +=1 
        else:
            if abs(pick - weitght) == 1:
                tired +=5
            elif abs(pick - weitght) == 2:
                tired +=25
    return tired
        
def solution(picks, minerals):
    answer = 0
    object_list = []
    divide_list = []
    total_pick = sum(picks)
    
    for index,mineral in enumerate(minerals):
        object_list.append(mineral)
        if (index+1) % 5 == 0:
            divide_list.append(object_list)
            object_list = []

        else:
            if index+1 == len(minerals):
                divide_list.append(object_list)

    queue = deque([])
    for index,count in enumerate(picks):
        if count != 0:
            queue.append([index,float('inf')])
            picks[index] -= 1
            break

    while queue :
        for i in divide_list:
            index,prev_tired = queue.pop()
            tired = prev_tired + check_tired(index,i)
            if tired < prev_tired :
                if picks[0] != 0 :
                    queue.append([0,tired])
                    picks[0] -= 1
                elif picks[1] != 0 :
                    queue.append([1,tired])
                    picks[1] -= 1
                elif picks[2] != 0 :
                    queue.append([2,tired])
                    picks[2] -= 1
            else:
                continue

    return answer


if __name__ == "__main__":
    test_input = {
        "picks":[1, 3, 2],
        "minerals":	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
    }

    test_input2 = {
        "picks":[0, 1, 1],
        "minerals":	["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
    }

    func_test = {
        "pick": 2,
        "divide_list":["diamond", "diamond", "diamond", "iron", "iron"]

    }
    check_tired(**func_test)
    assert(solution(**test_input)==12)
    assert(solution(**test_input2)==50)