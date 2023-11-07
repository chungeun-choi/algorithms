def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort(reverse=True)
    return candles.count(candles[0])


if __name__ == '__main__':
    candler = [4,2,3,1,2]
    result = birthdayCakeCandles(candler)
    print(result)