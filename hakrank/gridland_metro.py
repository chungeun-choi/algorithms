def gridlandMetro(n, m, k, track):
    track_map = {}
    result = 0
    for row,start,end in track:
        if row not in track_map:
            track_map[row] = []
        track_map[row].append((start,end))

    for row in track_map:
        track_map[row].sort()
        current_c2 = 0
        sum_track_value = 0

        for c1,c2 in track_map[row]:
            if c1 <= current_c2:
                if c2 > current_c2:
                    sum_track_value += c2 - current_c2
            else:
                sum_track_value += c2 - c1 + 1
            current_c2 = max(c2,current_c2)
        result += sum_track_value

    return n * m - result

if __name__ == "__main__":
    test_obj = [
        {
            "n":4,
            "m":4,
            "k":3,
            "track":[[2, 2, 3], [3, 1, 4], [4, 4, 4]]
        },
        {
            "n": 2,
            "m": 9,
            "k": 3,
            "track": [[2, 1, 5], [2, 2, 4], [2, 8, 8]]
        }
    ]
    '''
    2 9 3
    2 1 5
    2 2 4
    2 8 8
    '''

    print(gridlandMetro(**test_obj[1]))