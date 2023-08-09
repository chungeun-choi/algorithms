def solution(n, arr1, arr2):
    answer = []

    arr1_bytes = list(map(lambda x: format(x, 'b').rjust(n,'0'),arr1))
    arr2_bytes = list(map(lambda x: format(x, 'b').rjust(n,'0'),arr2))

    print(arr1_bytes)
    print(arr2_bytes)

    return answer


if __name__ == "__main__":
    test_input = {
        "n":5,
        "arr1":	[9, 20, 28, 18, 11],
        "arr2":[30, 1, 21, 17, 28]
    }

    assert(solution(**test_input)==["#####","# # #", "### #", "# ##", "#####"])