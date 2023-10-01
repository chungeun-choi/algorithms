from dateutil.relativedelta import relativedelta
from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    # 유통기한 리스트 생성
    terms_dict = dict()
    today = datetime.strptime(today,"%Y.%m.%d")

    for i in terms:
        name,date = i.split()
        terms_dict[name] = int(date)
    
    # 확인 로직
    for cnt,value in enumerate(privacies):
        regist_date,policy_name = value.split()
        # time delta 는 주간 밖에 해결 할 수 없음...
        expire_date = datetime.strptime(regist_date,"%Y.%m.%d") + relativedelta(months=terms_dict[policy_name])
        
        if today >= expire_date:
            answer.append(cnt+1)
        else:
            continue

    return answer