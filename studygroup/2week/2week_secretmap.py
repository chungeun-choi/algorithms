def solution(n, arr1, arr2):
    answer = []
    new_byte_array = list(zip(arr1, arr2))
    and_byte_array = list(map(lambda x: bin(x[0] | x[1]), new_byte_array))

    for cnt in range(0, n):
        value = and_byte_array[cnt]

        value = value.replace("0b", "")
        value = value.rjust(n, "0")
        value = value.replace("1", "#").replace("0", " ")

        answer.append(value)

    return answer


if __name__ == "__main__":
    test_input = {"n": 5, "arr1": [9, 20, 28, 18, 11], "arr2": [30, 1, 21, 17, 28]}

    test_input2 = {
        "n": 6,
        "arr1": [46, 33, 33, 22, 31, 50],
        "arr2": [27, 56, 19, 14, 14, 10],
    }
    assert solution(**test_input) == ["#####", "# # #", "### #", "#  ##", "#####"]
    assert solution(**test_input2) == [
        "######",
        "###  #",
        "##  ##",
        " #### ",
        " #####",
        "### # ",
    ]
