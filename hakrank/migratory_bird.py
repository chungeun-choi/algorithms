import collections
def migratoryBirds(arr):
    # Write your code here
    dict_value = collections.Counter(arr)
    result = sorted(dict_value.items(), key=lambda x: x[1], reverse=True)
    ret_val = [result[0][0]]
    for i in range(1,len(result)):
        if result[0][1] == result[i][1]:
            ret_val.append(result[i][0])

    return min(ret_val)

def migratoryBirds2(arr):
    # Write your code here
    freq = collections.Counter(arr)
    result = max(freq, key=freq.get)
    return result



if __name__ == "__main__":
    arr = [4,3,3,3,2,1]
    print(migratoryBirds(arr))
    print(migratoryBirds2(arr))