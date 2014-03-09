#! /usr/bin/python

def main():
	input = []
	file = open('67_input', 'r')
	for i in file:
		input.append(map(int, i.split(' ')))
	maxPath = maxPathSum(input, {}, 0, 0)
	print maxPath

def maxPathSum(input, dict, row, column):
	if (row, column) in dict.keys():
		return dict[(row, column)]
	if row > len(input)-1:
		return 0
	result = input[row][column] + max(maxPathSum(input, dict, row+1, column), 
		maxPathSum(input, dict, row+1, column+1))
	dict[(row, column)] = result
	return result

if __name__ == '__main__':
	main()