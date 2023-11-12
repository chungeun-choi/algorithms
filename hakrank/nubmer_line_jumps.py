x1, v1, x2, v2 = map(int, input().split())

if x1 > x2:
    if v2 > v1 and (x1-x2) % (v2-v1) == 0:
        print("YES")
    else:
        print("NO")
elif x1 < x2:
    if v1 > v2 and (x2-x1) % (v1-v2) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("YES")
