def pairs(k, arr):
    # Write your code here
    result = 0
    arr.sort()
    for pointer1 in range(0, len(arr)-1):
        pointer2 = pointer1+1
        diff = 0
        while diff <= k and pointer2 < len(arr):
            diff = arr[pointer2] - arr[pointer1]
            if diff == k:
                result += 1
                diff = 0
            pointer2 += 1
    return  result


if __name__ == "__main__":
    test_obj = [
        {
            "k": 2,
            "arr": [1,3,3,2,4,4,5,6,7],
            "required": 9
        }]

    for test_case in test_obj:
        k, arr, required = test_case.values()
        assert pairs(k,arr), required
