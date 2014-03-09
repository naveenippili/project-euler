#! /usr/bin/env python

def leastPow(number):
    for i in range(11):
        if i**number >= 10**(number-1):
            break
    return i

def main():
    sum = 0;
    for i in range(1,100):
        val = 10 - leastPow(i)
        if (val == 0):
            break
        sum += val
    print(sum)

if __name__ == '__main__':main()
