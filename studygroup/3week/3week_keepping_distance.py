from itertools import combinations


def check_wall(place,manhaten_list):
    for manhaten_object in manhaten_list:
        point1,point2 = manhaten_object 

        # 같은 x 선상 위에 존재
        if point1[0] == point2[0]:
            x = point1[0]
            y = point2[1] +1 if point1[1] > point2[1] else point1[1]+1

            if place[x][y] != "X":
                return False
            
        elif point1[1] == point2[1]:
            x = point2[0] +1 if point1[0] > point2[0] else point1[0]+1
            y = point1[1]

            if place[x][y] != "X":
                return False
        else :
            if place[point1[0]][point2[1]] == 'X' and place[point2[0]][point1[1]] == "X":
                continue
            else:
                return False

        return True
def solution(places):
    answer = []

    for place in places:
        p_position = []
        for x,value in enumerate(place) :
           p_position.extend([(x, cnt) for cnt,value in enumerate(value) if value == "P"]) 
        
        if len(p_position) == 0:
            answer.append(1)
            continue

        # 경우의 수 추출
        objects = list(combinations(p_position, 2))

        # 맨하튼 거리 계싼을 위한 lambda 함수
        func = lambda value: True if abs(value[1][0]-value[0][0])+abs(value[1][1]-value[0][1]) <= 2 else False
        # 맨하튼 거리가 2보다 작은 요소 추출
        manhaten_list = [value for value in objects if func(value)]
        
        
        if check_wall(place,manhaten_list):    
            answer.append(1)
        else:
            answer.append(0)

            
    return answer


if __name__ == "__main__":
    test_input = {
        "places": 
        [["POOOP", 
          "OXXOX", 
          "OPXPX", 
          "OOXOX", 
          "POXXP"], 
         ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
         ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
         ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    }


    print(solution(**test_input))