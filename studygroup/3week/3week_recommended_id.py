def solution(new_id):
    answer = ''
    return answer


if __name__ == "__main__":
    test_inputs = [
        {
            "new_id":"...!@BaT#*..y.abcdefghijklm",
        },
         {
            "new_id":"z-+.^.",
        },
         {
            "new_id":"=.=",
        },
         {
            "new_id":"123_.def",
        }
    ]

    assert(solution(**test_inputs[0])==	"bat.y.abcdefghi")