import re
from collections import Counter
def solution(s):
    answer = []
    
    numbers = re.findall(r'\d+', s)
    dict_list = Counter(numbers)
    sort_list = sorted(dict_list.items(), key = lambda item: item[1],reverse=True)

    answer = list(map(lambda x:int(x[0]),sort_list))

    return answer


if __name__ == "__main__":
    test_input = {
        "s":"{{2},{2,1},{2,1,3},{2,1,3,433}}"
    }

    assert(solution(**test_input)==[2, 1, 3, 4])