from collections import deque
if __name__ == "__main__":
    F,S,G,U,D = map(int,input().split())

    # 3 5 7 9 8 10
    building = [0] * (F + 1)
    q = deque()
    q.append(S)
    while q:
        x = q.popleft()
        if x == G:
            print(building[G])
            break
        for nx in [x + U, x - D]:
            if nx == x:
                continue
            if 0 < nx <= F and building[nx] == 0:
                building[nx] = building[x] + 1
                q.append(nx)
    else:
        print("use the stairs")