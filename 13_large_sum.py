#! /usr/bin/python

def main():
	input = []
	for i in xrange(100):
		input.append(long(raw_input()))

	sum1 = 0
	for i in xrange(100):
		sum1 += input[i]
	print sum1

	print sum([1,2,3])

if __name__ == '__main__':
	main()