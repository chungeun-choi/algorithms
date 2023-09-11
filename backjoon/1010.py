from itertools import permutations
def solution(west,east):
    
    pass


if __name__ == "__main__":
    input_list = []
    for i in range(int(input())):
        west,east = input().split()
        input_list.append((west,east))


    for west,east in input_list:
        print(solution(west,east))