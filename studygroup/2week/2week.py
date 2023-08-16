from collections import Counter


def solution(N, stages):
    answer = []
    peoples = len(stages)
    info_stay_stages = Counter(stages)

    for i in range(1, N + 1):
        value = info_stay_stages[i]
        if value == 0:
            answer.append((i, 0))
        else:
            failure = value / peoples
            peoples = peoples - value
            answer.append((i, failure))

    answer.sort(key=lambda x: x[1], reverse=True)
    answer = list(map(lambda x: x[0], answer))

    return answer


def solution2(numbers, hand):
    answer = ""
    """
    키패드 형태
    1 2 3   
    4 5 6
    7 8 9 
    *   #
    """

    left_pos = (3, 0)  # '*'
    right_pos = (3, 2)  # '#'

    key_pad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        "*": (3, 0),
        0: (3, 1),
        "#": (3, 2),
    }

    left_hands_list = [1, 4, 7, "*"]
    right_hands_list = [3, 6, 9, "#"]

    hands = {"right": "R", "left": "L"}

    # 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5
    for number in numbers:
        if number in left_hands_list:
            answer += "L"
            left_pos = key_pad[number]
            continue

        if number in right_hands_list:
            answer += "R"
            right_pos = key_pad[number]
            continue

        # 맨하튼 거리 계산법 - abs((x1-x2)) + abs((y1-y2))
        number_pos = key_pad[number]
        l_distance = abs(left_pos[0] - number_pos[0]) + abs(left_pos[1] - number_pos[1])
        r_distance = abs(right_pos[0] - number_pos[0]) + abs(
            right_pos[1] - number_pos[1]
        )

        if l_distance > r_distance:
            answer += "R"
            right_pos = key_pad[number]
        elif l_distance < r_distance:
            answer += "L"
            left_pos = key_pad[number]
        else:
            if "right" == hand:
                answer += hands[hand]
                right_pos = key_pad[number]
            else:
                answer += hands[hand]
                left_pos = key_pad[number]

    return answer


def solution3(today, terms, privacies):
    answer = []
    return answer


if __name__ == "__main__":
    # programmers - 실패율 [https://school.programmers.co.kr/learn/courses/30/lessons/42889]
    test1_input = {"N": 5, "stages": [2, 1, 2, 6, 2, 4, 3, 3]}

    test1_input2 = {"N": 4, "stages": [4, 4, 4, 4, 4]}
    assert solution(**test1_input) == [3, 4, 2, 1, 5]
    assert solution(**test1_input2) == [4, 1, 2, 3]

    # programmers - 키패드 누르기 [https://school.programmers.co.kr/learn/courses/30/lessons/67256]
    test2_input = {"numbers": [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "hand": "right"}

    test2_input2 = {"numbers": [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "hand": "left"}

    assert solution2(**test2_input) == "LRLLLRLLRRL"
    assert solution2(**test2_input2) == "LRLLRRLLLRR"
