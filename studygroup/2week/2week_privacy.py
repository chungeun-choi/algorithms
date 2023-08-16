from dateutil.relativedelta import relativedelta
from datetime import datetime


def solution(today, terms, privacies):
    answer = []
    # 유통기한 리스트 생성
    terms_dict = dict()
    today = datetime.strptime(today, "%Y.%m.%d")

    for i in terms:
        name, date = i.split()
        terms_dict[name] = int(date)

    # 확인 로직
    for cnt, value in enumerate(privacies):
        regist_date, policy_name = value.split()
        # time delta 는 주간 밖에 해결 할 수 없음...
        expire_date = datetime.strptime(regist_date, "%Y.%m.%d") + relativedelta(
            months=terms_dict[policy_name]
        )

        if today >= expire_date:
            answer.append(cnt + 1)
        else:
            continue

    return answer


if __name__ == "__main__":
    # programmers - 개인정보 수집 유효시간 [https://school.programmers.co.kr/learn/courses/30/lessons/150370]
    test3_input = {
        "today": "2022.05.19",
        "terms": ["A 6", "B 12", "C 3"],
        "privacies": ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
    }

    test3_input2 = {
        "today": "2020.01.01",
        "terms": ["Z 3", "D 5"],
        "privacies": [
            "2019.01.01 D",
            "2019.11.15 Z",
            "2019.08.02 D",
            "2019.07.01 D",
            "2018.12.28 Z",
        ],
    }

    assert solution(**test3_input) == [1, 3]
    assert solution(**test3_input2) == [1, 4, 5]
