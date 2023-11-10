def queensAttack(n, k, r_q, c_q, obstacles):
    result = 0
    # Write your code here
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            x = r_q + i
            y = c_q + j
            while 0 < x and x <= n and 0 < y and y <= n:
                if (x, y) in obstacles:
                    break
                x += i
                y += j
                result += 1
    return result


if __name__ == "__main__":
    # queensAttack(4,0,4,4,[])
    queensAttack(5, 3, 4, 3, [(5, 5), (4, 2), (2, 3)])
