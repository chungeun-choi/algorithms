from collections import deque
def solution(picks, minerals):
    answer = 0

    total_picsk = sum(picks)
    devide_minerals = []
    minium_minerals = []

    for cnt, i in enumerate(minerals):
        if cnt != 0 and cnt % 5 == 0:
            devide_minerals.append(minium_minerals)
            minium_minerals = []
        
        minium_minerals.append(i)
    
        if cnt == len(minerals) - 1:
            devide_minerals.append(minium_minerals)
        
    if len(devide_minerals) <= total_picsk:
        devide_minerals.sort(key = lambda x:(-x.count('diamond'),-x.count('iron'),-x.count('stone')))

    else:
        devide_minerals = devide_minerals[:total_picsk]
        devide_minerals.sort(key = lambda x:(-x.count('diamond'),-x.count('iron'),-x.count('stone')))
    
    mineral_type = {
        "diamond":0,
        "iron":1,
        "stone":2
    }

    
    

                    

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

    assert(solution(**test_input)==12)
    assert(solution(**test_input2)==50)