import re

def solution(dartResult):
    answer = 0
    parts = re.findall(r'\d+[SDT][*#]?', dartResult)

    section_infos = {
            "S": lambda x: x ,
            "D": lambda x: x*x,
            "T": lambda x: x*x*x
        }
    
    score_list = []

    
    for part in parts:
        # point 를 찾는 로직이 먼저 나와야함
        point = None
        calcurate = None
        option = None

        # 필요 키워드 파싱
        if part[:2].isdigit():
            point = part[:2]
            if len(part[2:]) == 2:
                calcurate = section_infos[part[2]]
                option = part[3]
            else:
                calcurate = section_infos[part[2]]
        else:
            if len(part) == 3:
                point,calcurate,option = part
                calcurate = section_infos[calcurate]
            else :
                point,calcurate = part
                calcurate = section_infos[calcurate]

        # 점수 계산
        if option == "*":
            if len(score_list)==0:
                value = calcurate(int(point))*2
                score_list.append(value)
            else:
                score_list[-1] = score_list[-1]*2 
                value = calcurate(int(point))*2
                score_list.append(value)
        elif option == "#":
            value = -calcurate(int(point))
            score_list.append(value)
        else:
            vlaue = calcurate(int(point))
            score_list.append(vlaue)
    
    answer = sum(score_list)
    
    return answer


if __name__ == "__main__":
    test_input = {
        "dartResult":"1S2D*3T",
    }

    test_input2 = {
        "dartResult":"1D2S#10S",
    }

    test_input3 = {
        "dartResult":"1D2S0T",
    }

    test_input4= {
        "dartResult":"1D2S3T*"
    }

    assert(solution(**test_input)==37)
    assert(solution(**test_input2)==9)
    assert(solution(**test_input3)==3)
    assert(solution(**test_input4)==59)