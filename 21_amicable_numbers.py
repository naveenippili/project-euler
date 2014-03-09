#! /usr/bin/env python

def main():
    sums = []
    for i in range(10000):
        sums.append(calculateDivisorSum(i))
    print(sums)
    amicableNumberSum = 0;
    for i in range(10000):
        try:
            if sums[sums[i]] == i and sums[i] != i:
                amicableNumberSum += i
                print('Adding: ', i)
        except:
            continue
    print(amicableNumberSum)

def calculateDivisorSum(number):
    if number == 0 or number == 1:
        return 0
    sum = 1
    for i in range(2, number):
        if (number % i == 0):
            if (number / i > i):
                sum += i
                sum += number/i
            elif (number /i == i):
                sum += i
            else:
                break;
    return int(sum)

if __name__ == '__main__':
    main()