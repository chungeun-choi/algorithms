from collections import deque
def solution(triangle):
    answer = 0
    visited = []
    stack = deque([])

    if len(triangle) == 0:
        return 0

    for i in triangle:
        visited.append([0 for _ in range(len(i))])
    
    stack.append(((0,0),0))

    while stack:
        pos, prev_value = stack.popleft()
        depth,nodes_number= pos
        
        sum_value = triangle[depth][nodes_number]+ prev_value
        if sum_value > visited[depth][nodes_number]:
            visited[depth][nodes_number] = sum_value

            next_depth = depth +1
            next_nodes_num = nodes_number +1

            if next_depth >= len(triangle):
                continue

            if next_nodes_num >= len(triangle[next_depth]):
                continue

            next_pos = (depth+1,nodes_number)
            nnext_pos = (depth+1, nodes_number+1)

            

            stack.extend([(next_pos,sum_value),(nnext_pos,sum_value)])

    answer = max(visited[-1])
    
    return answer




if __name__ == "__main__":
    __input = {
        "triangle": [[7], 
                     [3, 8], 
                     [8, 1, 0], 
                     [2, 7, 4, 4],
                     [4, 5, 2, 6, 5]]
    }

    assert(solution(**__input)==30)
    