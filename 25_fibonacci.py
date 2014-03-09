#! /usr/bin/env python

def main():
    a=[0,1,1]
    i = 3;
    while True:
        a.append(a[i-1] + a[i-2])
        if (a[i]>=10**999):
            break;
        i += 1
    print(i)

if __name__ == '__main__':main()
