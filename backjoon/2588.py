a=input()
b=input()

def solution(a,b):
    result1 = int(a) * int(b[2])
    result2 = int(a) * (int(b[1]))
    result3 = int(a) * (int(b[0]))

    return result1,result2,result3, int(a)*int(b)


for i in solution(a,b):
    print(i)