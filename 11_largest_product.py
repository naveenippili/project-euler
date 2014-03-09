#! /usr/bin/python

def main():
    input = []
    for i in xrange(20):
        input.append([])
        for j in raw_input().split(' '):
        	single_int = int(j);
        	input[i].append(single_int)
    print input
    print input[0][0] * input[0][1]

    max_sum = 0;

    for i in xrange(20):
        for j in xrange(20):
            if i+3 < 20:
                cur_sum = 1
                for k in xrange(4):
                    cur_sum *= input[i+k][j]
                max_sum = max(cur_sum, max_sum)
            if j+3 < 20:
                cur_sum = 1
                for k in xrange(4):
                    cur_sum *= input[i][j+k]
                max_sum = max(cur_sum, max_sum)
            if i+3<20 and j+3<20:
                cur_sum = 1
                for k in xrange(4):
                    cur_sum *= input[i+k][j+k]
                max_sum = max(cur_sum, max_sum)
            if i-3>=0 and j+3<20:
                cur_sum = 1
                for k in xrange(4):
                    cur_sum *= input[i-k][j+k]
                max_sum = max(cur_sum, max_sum)
    print 'max_sum: ' + str(max_sum)

if __name__ == '__main__':main()
