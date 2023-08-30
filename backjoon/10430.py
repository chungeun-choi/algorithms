a,b,c  = map(int,input().split())


def solution(a,b,c):
    
    result1 = (a+b)%c
    result2 = ((a%c)+(b%c))%c
    result3 = (a*b)%c
    result4 = ((a%c)*(b%c))%c

    return result1,result2,result3,result4


for i in solution(a,b,c):
    print(i)