#! /usr/bin/python

import time

def main():
    start = int(round(time.time() * 1000));
    i = 1;
    number = 0;
    while True:
        number += i;
        #print 'checking for: ' + str(number)
        divisorCount = calculateDivisorCount(number)
        #print 'divisorCount: ' + str(divisorCount)
        if divisorCount>= 500:
            print number
            break
        i = i+1
    end = int(round(time.time() * 1000));
    timeTaken = end - start;
    print 'timeTaken: ' + str(timeTaken)

def calculateDivisorCount(number):
    count = 0
    for i in xrange(1, number):
        if (number % i == 0):
            if (number / i > i):
                count += 2
            elif (number /i == i):
                count += 1
            else:
                break;
    return count

if __name__ == '__main__':main()