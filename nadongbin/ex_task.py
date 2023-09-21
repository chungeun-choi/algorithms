import sys
N,M,K = map(int,sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))

array.sort(reverse=True)
return_value = 0

count = K

for i in range(M):
    if count == 0:
        return_value += array[1]
        count = K
    else:
        return_value += array[0]
        count -=1

print(return_value)