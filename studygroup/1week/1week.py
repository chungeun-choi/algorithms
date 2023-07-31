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




if __name__ == "__main__":

    test_input = {
        "survey": ["AN", "CF", "MJ", "RT", "NA"],
        "choices": [5, 3, 2, 7, 5]

    }


    test_input2 = {
        "survey": ["TR", "RT", "TR"],
        "choices": [7, 1, 3]

    }


    assert(solution(**test_input2) =='RCJA')
    assert(solution(**test_input) =="TCMA")