def bonAppetit(bill, k, b):
    anna_value = sum(bill) - bill[k]
    if b > anna_value//2:
        return int(b - anna_value//2)
    else:
        return "Bon Appetit"
    # Write your code here


if __name__ == "__main__":
    bill = [3, 10, 2, 9]
    k = 1
    b = 12

    bill2 = [3, 10, 2, 9]
    k2 = 1
    b2 = 7
    result = bonAppetit(bill,k,b)
    result2 = bonAppetit(bill2,k2,b2)
    print(result)