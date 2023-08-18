def solution(picks, minerals):
    mineral_list=[]
    total_list =[]
    tired = 0
    dia_num = picks[0]
    iron_num = picks[1]
    stone_num = picks[2]
    total_num = dia_num + iron_num + stone_num
    for idx, i in enumerate(minerals):
        if idx != 0 and idx % 5 == 0:
            total_list.append(mineral_list)
            mineral_list = []

        mineral_list.append(i)
        if idx == len(minerals)-1:
            total_list.append(mineral_list)

    if len(total_list) <= total_num:
        total_list.sort(key = lambda x:(-x.count('diamond'),-x.count('iron'),-x.count('stone')))

    elif len(total_list) > total_num:
        total_list = total_list[:total_num]
        total_list.sort(key = lambda x:(-x.count('diamond'),-x.count('iron'),-x.count('stone')))


    for i in total_list:
        for idx, j in enumerate(i):
            if dia_num > 0:
                tired += 1

                if idx == len(i)-1:
                    dia_num -= 1

            elif dia_num == 0 and iron_num >0:
                if j == 'diamond':
                    tired += 5

                elif j == 'iron' or 'stone':
                    tired += 1

                if idx == len(i)-1:
                    iron_num -= 1

            elif dia_num ==0 and iron_num ==0 and stone_num >0:
                if j == 'diamond':
                    tired += 25

                elif j == 'iron':
                    tired += 5

                elif j == 'stone':
                    tired += 1

                if idx == len(i)-1:
                    stone_num -= 1
            if dia_num == 0 and iron_num == 0 and stone_num ==0:
                break

    return tired

