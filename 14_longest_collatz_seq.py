#! /usr/bin/python

def main():
	maxLength = 0
	maxNumber = 0
	for i in xrange(1000000):
		print 'current number: ' + str(i)
		length = getCollatzlen(i);
		if (length > maxLength):
			maxLength = length
			maxNumber = i

	print maxNumber;

def getCollatzlen(number):
	count = 1
	while number > 1:
		if number % 2 == 1:
			number = 3*number + 1
		else:
			number = number/2
		count += 1
	return count

if __name__ == '__main__':
	main()