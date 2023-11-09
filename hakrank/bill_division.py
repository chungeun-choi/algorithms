def bonAppetit(bill, k, b):
    anna_value = sum(bill) - bill[k]
    if b > anna_value // 2:
        return int(b - anna_value // 2)
    else:
        return "Bon Appetit"
    # Write your code here


if __name__ == "__main__":
    test_obj = [
        {
            "bill": [3, 10, 2, 9],
            "k": 1,
            "b": 12,
            "required": 5,
        },
        {
            "bill": [3, 10, 2, 9],
            "k": 1,
            "b": 7,
            "required": "Bon Appetit",
        },
    ]

    for test_case in test_obj:
        bill,k,b,required = test_case.values()
        assert bonAppetit(bill,k,b), required
