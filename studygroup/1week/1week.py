from itertools import islice


def solution(survey, choices):
    answer = ''
    type_dict = {
        'R':0,'T':0,
        'C':0,'F':0,
        'J':0,'M':0,
        'A':0,'N':0
    }
    point = [-3,-2,-1,0,1,2,3]
    

    #-3,-2,-1,0,1,2,3
    for cnt in range(0,len(survey)):
        typeA, typeB = survey[cnt] 
        select = point[choices[cnt]-1]

        if select >0 :
            type_dict[typeB] += select
        elif select == 0 :
            continue
        else: 
            type_dict[typeA] += abs(select)
    
    for i in range(0,8,2):
        slice_dcit = dict(islice(type_dict.items(), i,i+2))
        answer += max(slice_dcit,key=slice_dcit.get)


    return answer

def solution2(n,m):
    # 1억건의 input 값이라서 n 만큼 돌릴 수 없음 -> 탐색 문제가 아님에따라 DP를 사용해야함
    x= 0
    cnt = 1

    while True:
        x = (x+m)%n
        if x == 0:
            break
        else:
            cnt= cnt+1

    return cnt

def solution2_improve(n,m):
    # 많은 양의 데이터를 구하게 될 때  O(m+n)만큼의 시간이 걸리게됨
    # n과 m의 최대 공약수를 나누어 줌으로써 계산식 단축
    # 유클리드 호제법 : n,m(n>m)이고  r =  n%m 일 때, n과m의 최대공약수는 m과 r의 최대공약수와 같다
    
    a,b =n,m
    while (b):
        a,b= b,a%b
    gcd = a
    
    return n // gcd


from collections import Counter
# 1:6 , 2:5, 3:4, 4:3, 5:2 6:1
def solution3(lottos,win_nums):
    
    result = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }

    zero_count = Counter(lottos)[0]
    same_count = 0
    for i in range(0,len(lottos)):
        if lottos[i] in win_nums:
            same_count += 1
        else:
            continue
    
    return [result[same_count+zero_count],result[same_count]]


def solution4(s):
    answer = 0
    queue = []
    value = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }

    change_points = []

    for cnt,char in enumerate(s) :
        if char.isdigit():
            continue
        else:
            queue.append(char)
            keyword = "".join(queue).lower()
            if keyword in value :
                queue = []
                change_points.append(keyword)
    
    for change_object in change_points:
        s = s.replace(change_object,str(value[change_object]))

    answer = int(s)

    return answer


if __name__ == "__main__":

    test_solution1_input = {
        "survey": ["AN", "CF", "MJ", "RT", "NA"],
        "choices": [5, 3, 2, 7, 5]

    }


    test_solution1_input2 = {
        "survey": ["TR", "RT", "TR"],
        "choices": [7, 1, 3]

    }


    

    assert(solution(**test_solution1_input2) =='RCJA')
    assert(solution(**test_solution1_input) =="TCMA")



    test_solution2_input = {    
        "n":10,
        "m":4
    }

    test_solution2_input2 = {
        "n": 947853,
        "m":4453

    }


    assert(solution2(**test_solution2_input)==5)
    assert(solution2_improve(**test_solution2_input2)==947853)



    test_solution3_input1 = {
        "lottos":[44, 1, 0, 0, 31, 25],
        "win_nums":[31, 10, 45, 1, 6, 19]
    }

    assert(solution3(**test_solution3_input1) ==[3,5])



    test_solution4_input1 = {
        "s" : "one4seveneight"
    }

    test_solution4_input2 = {
        "s" : "oneoneoneone"
    }

    assert(solution4(**test_solution4_input2)==1000)