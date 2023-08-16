from datetime import datetime,timedelta
import math
def solution(fees, records):
    answer = []

    parking_history = {}
    pay_history = {}

    for record in records:
        time,car_number,action = record.split()

        if car_number not in parking_history:
            parking_history.setdefault(car_number,{action:datetime.strptime(time,"%H:%M")})
            pay_history.setdefault(car_number,0)
        
        else:
            if action == "OUT":
                result_time =datetime.strptime(time,"%H:%M") - parking_history[car_number]["IN"] 
                parking_time = result_time.total_seconds()/60
                parking_history.pop(car_number)
                if car_number not in pay_history:
                    pay_history.setdefault(car_number,parking_time)
                else:
                    pay_history[car_number] += parking_time
    
    # 입차 한 뒤 출차 안한 기록 계산
    for car_number,value in parking_history.items():
        parking_time = (datetime.strptime("23:59","%H:%M")- value["IN"]).total_seconds()/60
        pay_history[car_number] += parking_time

    pay_history = dict(sorted(pay_history.items()))


    for pay in pay_history.values():
        # fees 기본시간, 기본 요금. 할당 요금 분, 할당 요금
        if pay > fees[0]:
            result = fees[1] + math.ceil((pay-fees[0])/fees[2])*fees[3]
            answer.append(result)
        else:
            answer.append(fees[1])

    return answer


if __name__ == "__main__":
    test_input = {
        "fees": [180, 5000, 10, 600],
        "records": [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    }

    test_inpu2 = {
        "fees":[1, 461, 1, 10],
        "records":["00:00 1234 IN"]
    }

    solution(**test_input)
    solution(**test_inpu2)
