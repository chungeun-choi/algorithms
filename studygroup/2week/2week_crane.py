def solution(board, moves):
    answer = 0
    queue = []
    

    for move in moves :
        for cnt in range(0,len(board)):
            print("boar pos: {} , board value: {}".format((cnt,move-1),board[cnt][move-1]))
            if board[cnt][move-1] != 0:
                if queue: 
                    if queue[-1] == board[cnt][move-1]:
                        queue.pop() 
                        board[cnt][move-1]= 0
                        answer +=2
                        break
                    else:
                        queue.append(board[cnt][move-1])
                        board[cnt][move-1] = 0
                        break
                else :
                    queue.append(board[cnt][move-1])
                    board[cnt][move-1] = 0
                    break
            else:
                continue

    return answer



if __name__ == "__main__":
    test_input = {
        "board":[[0,0,0,0,0],
                 [0,0,1,0,3],
                 [0,2,5,0,1],
                 [4,2,4,4,2],
                 [3,5,1,3,1]],
        "moves":[1,5,3,5,1,2,1,4]
    }
    assert(solution(**test_input)==4)