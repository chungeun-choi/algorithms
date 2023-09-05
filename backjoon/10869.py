# A+B, A-B, A*B, A/B(몫), A%B

a, b = input().split()


def solution(a, b):
    a = int(a)
    b = int(b)

    p = a + b
    m = a - b
    e = a * b
    d = a // b
    t = a % b

    return p, m, e, d, t


for i in solution(a, b):
    print(i)
