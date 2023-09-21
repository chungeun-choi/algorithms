import sys
n = int(sys.stdin.readline())
count = 0

value = 1000 - n
mod_value = [500,100,50,10,5,1]
#500엔, 100엔, 50엔, 10엔, 5엔, 1엔
for i in mod_value:
    if value == 0:
        break
    value,mod = divmod(value,i)
    count += value
    value = mod
    

print(count)